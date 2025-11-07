# COVID Data Pipeline

Simple ETL pipeline that:
- reads `covid_data.csv`
- cleans & transforms with pandas
- loads to PostgreSQL (`covid_stats` table)
- generates visualizations (Matplotlib)

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
   
3. Create .env from template and edit:
   ```bash
   cp .env.template .env
   #then edit .env with your DB password

4. Run the pipeline:
   ```bash
   source venv/bin/activate
   python3 covid_pipeline.py
 
