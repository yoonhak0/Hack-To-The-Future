# Microeconomic trends in CRE
This project explores the relationship between Real GDP, Taxes, and Unemployment across different corporate locations. The analysis includes various visualizations to highlight trends, correlations, and insights, including:

3 Heatmaps to represent the geographic distribution and correlation of Real GDP, Taxes, and Unemployment.

A Bar Chart comparing A properties and O properties across different regions.

A Regression Line Plot to demonstrate the relationship between Taxes and Real GDP.

Project Features
Heatmaps: Visualize spatial trends and patterns of Real GDP, Taxes, and Unemployment by corporate location.

Bar Chart: Compares A properties and O properties across different regions, highlighting differences in property types and regional trends.

Regression Line Plot: A linear regression analysis to uncover any significant relationships between Real GDP, Taxes, and Unemployment.

Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/real-gdp-taxes-unemployment.git
Navigate to the project directory:

bash
Copy
Edit
cd real-gdp-taxes-unemployment
Install the necessary dependencies using pip (recommended to use a virtual environment):

bash
Copy
Edit
pip install -r requirements.txt
The requirements.txt file includes all the necessary packages for the project:

pandas

plotly

matplotlib (for any additional visualizations)

seaborn (for enhanced plots)

Dataset
The project uses data on Real GDP, Taxes, Unemployment, and Property Types across various corporate locations. The data is stored in CSV format and can be loaded into the project using the pd.read_csv() method.

Real GDP: Economic output data for various locations.

Taxes: Corporate tax rates for different regions.

Unemployment: Unemployment rate data by location.

Property Type: Identifies whether the property is an A property or O property.

Data Format:
The dataset should contain the following columns:

location: Name of the corporate location.

gdp: Real GDP data for the location.

taxes: Corporate tax rates.

unemployment: Unemployment rates for the location.

property_type: Indicates whether the property is an A property or O property.

region: The region where the location is situated.

Usage
Load the dataset into the project by adjusting the file path in the code.

Execute the Python script or Jupyter notebook to generate the visualizations.

Customize the heatmaps, bar chart, and regression plots by modifying the column names and visual attributes in the code.

Example Usage:
python
Copy
Edit
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("your-data-file.csv")

# Generate heatmap for Real GDP
fig = px.density_mapbox(df, lat='latitude', lon='longitude', z='gdp', radius=10, mapbox_style="stamen-terrain")
fig.show()

# Generate bar chart comparing A properties and O properties across regions
fig = px.bar(df, x='region', y=['A properties', 'O properties'], barmode='group', title="A vs O Properties by Region")
fig.show()

# Create regression line plot for Taxes vs. Real GDP
fig = px.scatter(df, x='taxes', y='gdp', trendline="ols")
fig.show()
Visualizations
Heatmaps:
Real GDP Heatmap: Shows the intensity of Real GDP across different locations.

Taxes Heatmap: Displays the spatial distribution of taxes across regions.

Unemployment Heatmap: Visualizes unemployment rate variations across corporate locations.

Bar Chart:
Compares A properties and O properties across various regions, highlighting property type distribution in each area.

Regression Line Plot:
Shows the relationship between Taxes and Real GDP, with a regression line to highlight the trend.
