import pandas as pd

# Load dataset (replace with the path to your actual CSV file)
df = pd.read_csv("price and availability data.csv")

# Define city-region assignments (one representative per region)
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
    # Add more cities as needed, ensuring only one per region
}

# Ensure only one city per region gets assigned
regions_assigned = set()
def assign_region(city):
    # If region is already assigned, return None to avoid duplicates
    region = city_region_map.get(city)
    if region and region not in regions_assigned:
        regions_assigned.add(region)
        return region
    return None

# Apply region assignment to the cities in the DataFrame
df['Region'] = df['market'].apply(assign_region)

# Handle any cities that weren't assigned a region due to duplicates or missing data
df['Region'].fillna('Unknown', inplace=True)

# Display the updated DataFrame with regions assigned
print(df[['market', 'Region']])

# Save the results to a new CSV file (optional)
df.to_csv("city_region_assigned.csv", index=False)

# Optional: Display the first few rows of the updated DataFrame
df.head()
