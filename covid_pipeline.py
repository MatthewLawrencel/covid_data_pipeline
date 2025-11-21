import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

# -----------------------------------------------------
# Load CSV (same folder as this script)
# -----------------------------------------------------
file_path = "covid_data.csv"

try:
    df = pd.read_csv(file_path)
    print("CSV loaded successfully")
except FileNotFoundError:
    print("Error: covid_data.csv not found in project folder.")
    exit()

# -----------------------------------------------------
# Select required columns
# -----------------------------------------------------
required_columns = [
    "location", "date", "total_cases", "new_cases",
    "total_deaths", "new_deaths", "population"
]

missing = set(required_columns) - set(df.columns)
if missing:
    print(f"Missing required columns in CSV: {missing}")
    exit()

df = df[required_columns]

# Clean data
df.dropna(subset=["total_cases", "total_deaths"], inplace=True)
df["date"] = pd.to_datetime(df["date"], errors="ignore")

# -----------------------------------------------------
# Connect to PostgreSQL
# -----------------------------------------------------
DB_URL = "postgresql+psycopg2://postgres:matthew123@localhost:5432/covid_db"

try:
    engine = create_engine(DB_URL)
    print("Connected to PostgreSQL")
except Exception as e:
    print("Database connection failed:", str(e))
    exit()

# -----------------------------------------------------
# Load into database
# -----------------------------------------------------
try:
    df.to_sql("covid_stats", engine, if_exists="replace", index=False)
    print("Data loaded into covid_stats table")
except Exception as e:
    print("Error writing to database:", str(e))
    exit()

# -----------------------------------------------------
# Query DB
# -----------------------------------------------------
query = """
SELECT location AS country, MAX(total_cases) AS total_cases
FROM covid_stats
GROUP BY location
ORDER BY total_cases DESC;
"""

try:
    result_df = pd.read_sql(query, engine)
    print("Query executed successfully")
except Exception as e:
    print("Query error:", str(e))
    exit()

# -----------------------------------------------------
# Visualization (Top 20)
# -----------------------------------------------------
top = result_df.head(20).sort_values(by="total_cases", ascending=True)

plt.figure(figsize=(12, 6))
plt.barh(top["country"], top["total_cases"], edgecolor="black")
plt.xlabel("Total Cases")
plt.ylabel("Country")
plt.title("Top 20 Total COVID-19 Cases by locations")
plt.tight_layout()
plt.show()
