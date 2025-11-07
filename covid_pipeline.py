import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

# Load data from CSV file
file_path = "covid_data.csv"
df = pd.read_csv(file_path)

# Select only required columns
columns = ["location", "date", "total_cases", "new_cases", "total_deaths", "new_deaths", "population"]
df = df[columns]

# Drop rows with missing total_cases or total_deaths
df.dropna(subset=["total_cases", "total_deaths"], inplace=True)

# Connect to PostgreSQL
engine = create_engine("postgresql+psycopg2://postgres:matthew123@localhost:5432/covid_db")

# Create table and load data
df.to_sql("covid_stats", engine, if_exists="replace", index=False)

# Query to load data for countries with maximum cases
query = """
SELECT location AS country, MAX(total_cases) AS total_cases
FROM covid_stats
GROUP BY country
ORDER BY total_cases DESC;
"""
df = pd.read_sql(query, engine)

# visualization – show only top 20 countries for clarity
plt.figure(figsize=(12, 6))
plt.barh(df['country'].head(20)[::-1], df['total_cases'].head(20)[::-1], color='skyblue', edgecolor='black')
plt.xlabel("Total Cases", fontsize=12)
plt.ylabel("Country", fontsize=12)
plt.title("Top Locations with Maximum Total COVID-19 Cases", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

