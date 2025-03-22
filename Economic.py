import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("price and availability data.csv")

# Remove the row where market is "US National"
df = df[df["market"] != "US National"]

# Define region assignment based on cities
city_region_map = {
    "New York": "North East",
    "Boston": "North East",
    "Philadelphia": "North East",
    "Washington D.C.": "North East",
    "Chicago": "Midwest",
    "Detroit": "Midwest",
    "Minneapolis": "Midwest",
    "Cleveland": "Midwest",
    "Los Angeles": "West",
    "San Francisco": "West",
    "Seattle": "West",
    "San Diego": "West",
    "Dallas": "South",
    "Houston": "South",
    "Miami": "South",
    "Atlanta": "South",
    "Denver": "West",
    "Phoenix": "West",
    "St. Louis": "Midwest",
    "Indianapolis": "Midwest",
    "Charlotte": "South",
    "Tampa": "South",
    "Orlando": "South",
    # Add more cities here as needed
}

# Function to assign region to a city
def assign_region(city):
    return city_region_map.get(city, 'Unknown')  # Default to 'Unknown' if city is not in the map

# Assign region to each city in the market column
df['Region'] = df['market'].apply(assign_region)

# Remove rows where Region is "Unknown"
df = df[df['Region'] != 'Unknown']

# Define threshold for "high supply & demand" (adjust as needed)
high_supply_threshold = df["available_space"].quantile(0.75)  # Top 25% supply
high_demand_threshold = df["leasing"].quantile(0.75)  # Top 25% demand

# Identify "investment-worthy" markets
df["investment_target"] = (df["available_space"] >= high_supply_threshold) & (df["leasing"] >= high_demand_threshold)

# Adjust bubble size: Size proportional to available space
df["size"] = df["available_space"] / df["available_space"].max() * 1000

# Function to create a plot for a specific region
def create_region_plot(region):
    # Assign colors: Highlight the selected region in green, others in gray
    df["color"] = df["Region"].apply(lambda x: "green" if x == region else "gray")
    
    # Create Plotly figure
    fig = px.scatter(df, x="leasing", y="available_space",  # Compare Leasing (demand) and Available Space (supply)
                     color="Region",  # Color-code by region (for legend)
                     size="size",  # Highlight cities with bigger bubbles based on available space
                     hover_data=["market", "available_space", "leasing", "Region"],  # Show city and additional info on hover
                     title=f"Supply vs. Demand: Leasing vs. Available Space (Highlighting {region})",
                     trendline="ols",  # Add a linear regression line
                     trendline_scope="overall",  # Ensure only one regression line for the entire dataset
                     color_discrete_map={
                         "South": "gray",
                         "West": "gray",
                         "North East": "gray",
                         "Midwest": "gray",
                         region: "red"  # Override the focused region to red
                     })
    
    # Modify the appearance of the trendline (make it black and bold)
    fig.update_traces(line=dict(color='black', width=4))  # Change line color to black and increase width

    # Customize legend (scrollable)
    fig.update_layout(legend=dict(
        yanchor="top", y=1, xanchor="left", x=1.02,  # Position outside plot
        title="Regions", font=dict(size=12),  # Adjust text size
        bgcolor="rgba(255,255,255,0.6)",  # Transparent background
        itemsizing="trace", traceorder="normal"  # Keep order clean
    ))
    
    # Change axis labels
    fig.update_layout(
        xaxis_title="Leasing Demand",  # Change X-axis label
        yaxis_title="Available Space (Supply)"  # Change Y-axis label
    )
    
    # Show interactive plot
    fig.show()

# Create plots for each region
regions = ["South", "West", "North East", "Midwest"]
for region in regions:
    create_region_plot(region)
