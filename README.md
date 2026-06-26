# Climate Data ETL Pipeline

## Overview

This project demonstrates a production-style, end-to-end ETL (Extract, Transform, Load) pipeline for historical weather data using **Python, Pandas, SQLite, SQL, and the Open-Meteo Archive API**.

The pipeline automatically extracts daily weather observations for multiple German cities, performs data cleaning and quality validation, stores analysis-ready datasets in both CSV and SQLite formats, validates the resulting database using SQL queries, generates analytical summaries, and produces publication-quality visualizations.

The project demonstrates practical data engineering principles including:

- API integration
- Modular software architecture
- Configuration-driven workflows
- Automated ETL orchestration
- Data quality validation
- SQL database management
- Climate data analysis
- Scientific visualization
- Logging and reporting
- Reproducible software development using Git and GitHub

---

# Project Goals

- Extract historical weather observations from a public API
- Automate data ingestion for multiple cities
- Clean and transform raw datasets
- Perform automated data quality validation
- Store processed datasets in CSV and SQLite formats
- Validate database integrity using SQL
- Generate climate analytics using SQL queries
- Produce publication-quality visualizations
- Demonstrate reproducible ETL pipeline development

---

# Technologies

- Python
- Pandas
- NumPy
- Requests
- SQLite
- SQL
- Matplotlib
- Jupyter Notebook
- Git
- GitHub

---

# Supported Cities

The pipeline currently processes daily historical weather observations for:

- Hannover
- Berlin
- Hamburg
- Munich
- Cologne

---

# Climate Variables

The ETL pipeline retrieves:

- Daily Mean Temperature
- Daily Maximum Temperature
- Daily Minimum Temperature
- Daily Precipitation

Derived variables include:

- Month
- Year
- City

---

# Project Structure

```text
climate-data-etl/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── weather.db
│
├── outputs/
│   ├── analysis/
│   ├── figures/
│   ├── logs/
│   └── reports/
│
├── notebooks/
│
├── src/
│   ├── analyze.py
│   ├── config.py
│   ├── extract.py
│   ├── load.py
│   ├── logger.py
│   ├── pipeline.py
│   ├── quality.py
│   ├── report.py
│   ├── transform.py
│   ├── validate.py
│   └── visualize.py
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
          Data Quality Validation
              (quality.py)
                      │
                      ▼
            Clean CSV Files
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
             analyze.py (SQL)
                      │
                      ▼
            visualize.py
                      │
                      ▼
      Reports • Analysis • Figures
```

The complete workflow is orchestrated automatically by `pipeline.py`.

---

# Running the Pipeline

Execute the ETL pipeline:

```bash
python3 src/pipeline.py
```

The pipeline automatically performs:

1. Extract weather observations from the Open-Meteo Archive API
2. Save raw CSV files
3. Clean and transform datasets
4. Perform automated quality validation
5. Load data into SQLite
6. Validate the database
7. Generate an ETL run summary

---

# Climate Analysis

Run SQL-based analyses:

```bash
python3 src/analyze.py
```

The analysis module automatically generates:

- Average temperature by city
- Annual precipitation by city
- Warmest days
- Coldest days
- Monthly climate summary

Outputs are saved to:

```text
outputs/analysis/
```

---

# Climate Visualizations

Generate visualizations:

```bash
python3 src/visualize.py
```

The visualization module produces:

### 1. Average Temperature by City

- Bar Chart

### 2. Annual Precipitation by City

- Bar Chart

### 3. Monthly Climate Dynamics

- Dual-axis combination chart
- Monthly precipitation
- Monthly average temperature

### 4. Temperature Profiles & Volatility

- Box plots for:
  - Mean Temperature
  - Maximum Temperature
  - Minimum Temperature

### 5. Heavy Rainfall Distribution

- Box plot of precipitation
- Rainy days only

Figures are saved to:

```text
outputs/figures/
```

---

# Data Quality Validation

Each processed dataset is automatically checked for:

- Missing values
- Duplicate city-date records
- Temperature consistency
- Negative precipitation
- Expected row count

Results are recorded in the pipeline logs.

---

# Database Validation

After loading, SQLite validation confirms:

- Database creation
- Table existence
- Column schema
- Row count
- Date range
- Sample records

Current database statistics:

| Metric | Value |
|---------|------:|
| Cities | 5 |
| Rows per city | 366 |
| Total observations | 1,830 |

---

# Logging

The pipeline uses structured logging.

Log file:

```text
outputs/logs/pipeline.log
```

Logged events include:

- API requests
- Extraction progress
- Transformation
- Quality checks
- Database loading
- Database validation
- Analysis execution
- Visualization generation
- ETL completion

---

# Automated ETL Report

Each pipeline execution generates a summary report.

Example:

```text
outputs/reports/etl_summary.txt
```

The report includes:

- Run status
- Cities processed
- Rows processed
- Rows loaded
- Rows per city
- Database table
- Date range
- Data quality summary
- Timestamp

---

# SQLite Schema

Current table:

```text
weather_data
```

| Column | Description |
|---------|-------------|
| date | Observation date |
| mean_temp | Daily mean temperature |
| max_temp | Daily maximum temperature |
| min_temp | Daily minimum temperature |
| precipitation | Daily precipitation |
| city | Source city |
| month | Extracted month |
| year | Extracted year |

---

# Completed Features

## Version 1.0

- Open-Meteo API integration
- Basic ETL pipeline
- SQLite loading
- Database validation

## Version 2.0

- Configuration-driven workflow
- Multi-city processing
- Dynamic file naming
- Reusable pipeline

## Version 3.0

- Structured logging
- Data quality validation
- ETL summary reporting
- Production-ready pipeline

## Version 4.0

- SQL analytics module
- Climate analysis queries
- Publication-quality visualizations
- Box plots
- Automated reporting
- Modular analytics workflow

---

# Future Enhancements (Version 5.0)

Planned improvements include:

- Interactive Streamlit dashboard
- Plotly visualizations
- Climate anomaly detection
- Multi-year comparisons
- Automated unit testing
- Docker containerization
- GitHub Actions CI/CD
- PostgreSQL backend
- Airflow orchestration
- Cloud deployment

---

# License

This repository is intended for educational, research, and portfolio purposes.