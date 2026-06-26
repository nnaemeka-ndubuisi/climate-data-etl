# Climate Data ETL Pipeline

## Overview

This project demonstrates a configurable, end-to-end ETL (Extract, Transform, Load) pipeline for historical weather data using **Python, Pandas, SQLite, and the Open-Meteo Archive API**.

The pipeline automatically extracts daily weather observations for multiple German cities, performs data cleaning and feature engineering, executes automated data quality checks, stores analysis-ready datasets in both CSV and SQLite formats, validates the resulting database using SQL queries, and generates execution logs and summary reports.

The project showcases practical data engineering principles including API integration, modular software design, configuration-driven workflows, data validation, SQL database management, structured logging, automated reporting, and reproducible ETL development using Git and GitHub.

---

# Project Goals

* Extract historical weather observations from a public API
* Automate data ingestion for multiple cities
* Clean and transform raw datasets
* Perform automated data quality validation
* Store processed data in CSV and SQLite formats
* Validate database integrity using SQL queries
* Generate ETL execution reports
* Demonstrate reproducible ETL pipeline development
* Provide a foundation for future climate analytics

---

# Technologies

* Python
* Pandas
* NumPy
* Requests
* SQLite
* Matplotlib
* Jupyter Notebook
* Git & GitHub

---

# Supported Cities

The pipeline currently processes historical daily weather observations for:

* Hannover
* Berlin
* Hamburg
* Munich
* Cologne

---

# Climate Variables

* Daily Mean Temperature
* Daily Maximum Temperature
* Daily Minimum Temperature
* Daily Precipitation

---

# Project Structure

```text
climate-data-etl/
├── data/
│   ├── raw/
│   ├── processed/
│   └── weather.db
│
├── notebooks/
│
├── outputs/
│   ├── figures/
│   ├── logs/
│   │   └── pipeline.log
│   └── reports/
│       └── etl_summary.txt
│
├── src/
│   ├── config.py
│   ├── extract.py
│   ├── transform.py
│   ├── quality.py
│   ├── load.py
│   ├── validate.py
│   ├── report.py
│   ├── logger.py
│   └── pipeline.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# ETL Architecture

```text
                config.py
                     │
                     ▼
        Open-Meteo Archive API
                     │
                     ▼
               extract.py
                     │
                     ▼
               Raw CSV Files
                     │
                     ▼
             transform.py
                     │
                     ▼
          quality.py (QA Checks)
                     │
                     ▼
          Processed CSV Files
                     │
                     ▼
                load.py
                     │
                     ▼
            SQLite Database
                     │
                     ▼
             validate.py
                     │
                     ▼
              report.py
                     │
                     ▼
      ETL Summary + Pipeline Logs
```

The entire workflow is orchestrated automatically by `pipeline.py`, allowing the pipeline to process every configured city without manual intervention.

---

# Example Workflow

Run the complete pipeline:

```bash
python3 src/pipeline.py
```

For each configured city, the pipeline automatically performs the following steps:

1. Read city configuration
2. Extract historical weather observations from the Open-Meteo Archive API
3. Store raw observations as CSV
4. Clean and transform the dataset
5. Perform automated data quality checks
6. Load processed data into SQLite
7. Validate the SQLite database
8. Generate an ETL execution summary
9. Record structured pipeline logs

---

# Generated Outputs

## Raw Data

```text
data/raw/
```

Example:

```text
hannover_weather_2024.csv
berlin_weather_2024.csv
hamburg_weather_2024.csv
munich_weather_2024.csv
cologne_weather_2024.csv
```

---

## Processed Data

```text
data/processed/
```

Example:

```text
hannover_weather_2024_clean.csv
berlin_weather_2024_clean.csv
hamburg_weather_2024_clean.csv
munich_weather_2024_clean.csv
cologne_weather_2024_clean.csv
```

---

## SQLite Database

```text
data/weather.db
```

Database table:

```text
weather_data
```

Current schema:

| Column        | Description               |
| ------------- | ------------------------- |
| date          | Observation date          |
| mean_temp     | Daily mean temperature    |
| max_temp      | Daily maximum temperature |
| min_temp      | Daily minimum temperature |
| precipitation | Daily precipitation       |
| city          | Source city               |
| month         | Month extracted from date |
| year          | Year extracted from date  |

---

## ETL Summary Report

```text
outputs/reports/etl_summary.txt
```

The automatically generated report includes:

* Pipeline execution status
* Cities processed
* Rows processed
* Rows loaded
* Rows per city
* Database table name
* Date range
* Data quality check results
* Execution timestamp

---

## Pipeline Logs

```text
outputs/logs/pipeline.log
```

Structured logs capture every stage of the ETL workflow, including:

* API requests
* Weather data extraction
* Data transformation
* Data quality validation
* Database loading
* Database validation
* Report generation
* Pipeline completion status

---

# Database Validation

The validation module automatically verifies:

* Database creation
* Table existence
* Database schema
* Total rows loaded
* Date range consistency
* Sample records
* Successful completion of the ETL workflow

Current pipeline statistics:

* **Cities processed:** 5
* **Observations per city:** 366
* **Total observations:** 1,830

---

# Data Quality Validation

Before loading data into SQLite, the pipeline automatically performs several quality assurance checks:

* Missing value detection
* Duplicate city-date detection
* Temperature consistency validation
* Negative precipitation detection
* Expected row count verification

Quality metrics are included in the ETL execution summary.

---

# Completed Features

* Repository initialization
* Modular ETL architecture
* Configuration-driven workflow
* Multi-city weather extraction
* Open-Meteo Archive API integration
* Automated data cleaning
* Feature engineering
* Automated data quality validation
* SQLite database integration
* SQL-based database validation
* Structured pipeline logging
* Automated ETL execution reports
* Dynamic file naming
* Reusable pipeline design

---

# Future Enhancements

* Climate trend visualizations
* Interactive dashboards (Streamlit/Dash)
* Unit testing with pytest
* Additional weather variables
* PostgreSQL backend
* Docker containerization
* CI/CD using GitHub Actions
* Automated scheduling (Apache Airflow/Cron)
* Data warehouse integration

---

# License

This project is intended for educational and portfolio purposes.
