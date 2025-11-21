# COVID Data Pipeline

This project demonstrates a simple **data engineering workflow** for processing, storing, and visualizing COVID-19 data using Python, Pandas, PostgreSQL, and Matplotlib.


## Project Overview

The goal of this project is to build a pipeline that:
1. **Extracts** COVID-19 data from a CSV file.
2. **Transforms** the data by selecting relevant columns and cleaning missing values.
3. **Loads (ETL)** the data into a PostgreSQL database.
4. **Visualizes** the top countries with the highest total COVID-19 cases.

---

## Project Structure
```bash
covid_data_pipeline/
├── covid_data.csv
├── covid_pipeline.py
├── requirements.txt
├── LICENSE
└── README.md
```

## Tech Stack

- **Python 3**
- **Pandas** – Data manipulation
- **SQLAlchemy** – Database connectivity
- **PostgreSQL** – Data storage
- **Matplotlib** – Data visualization

---

## Files
- `covid_pipeline.py` — main script
- `covid_data.csv` — (not committed; download or place locally)
- `requirements.txt` — Python deps
- `.env.template` — environment variable template

## Setup (local)

1. Create virtualenv and install:
   ```bash
   python3 -m venv venv
   source venv/bin/activate

2. Create Postgres DB:
   ```bash           
   sudo -u postgres psql
   CREATE DATABASE covid_db;
   \q
   

3. Run the pipeline:
   ```bash
   source venv/bin/activate
   python3 covid_pipeline.py

## Example Output

   A horizontal bar graph showing:
   X-axis: Total COVID-19 cases
   Y-axis: Locations
   Top 20 locations displayed in descending order.

# Author
  Matthew Lawrence L
  
  Gmail:lawrence82773824@gmail.com
  lawrence82773824@gmail.com
  
 
