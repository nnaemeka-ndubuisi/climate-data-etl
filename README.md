# Climate Data ETL Pipeline

## Overview

This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline for historical climate data using Python, Pandas, SQLite, and the Open-Meteo API.

The pipeline automates the extraction of weather observations, performs data cleaning and feature engineering, stores processed datasets, and loads analysis-ready data into a SQLite database for querying and downstream analytics.

The project showcases practical data engineering, environmental data analytics, API integration, and reproducible workflow development using Git and GitHub.


---

## Project Goals

- Extract historical climate data from public APIs
- Clean and validate raw datasets
- Transform data into analysis-ready formats
- Store processed data in CSV and SQLite formats
- Generate exploratory climate analyses and visualisations
- Demonstrate reproducible ETL pipeline development

---

## Technologies

- Python
- Pandas
- NumPy
- Requests
- SQLite
- Matplotlib
- Jupyter Notebook
- Git & GitHub

---

## Current City

- Hannover

---

## Climate Variables

- Daily Mean Temperature
- Daily Maximum Temperature
- Daily Minimum Temperature
- Daily Precipitation

---

## Project Structure

```text
climate-data-etl/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── outputs/
│   └── figures/
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── pipeline.py
├── README.md
├── requirements.txt
└── .gitignore
```

---
## ETL Architecture

```text
Open-Meteo API
        ↓
extract.py
        ↓
Raw CSV
        ↓
transform.py
        ↓
Processed CSV
        ↓
load.py
        ↓
SQLite Database
        ↓
pipeline.py
```

## Example Workflow

```bash
python3 src/pipeline.py
```

This command executes the complete ETL workflow:

1. Extract weather data from the Open-Meteo API
2. Store raw observations as CSV
3. Clean and transform the dataset
4. Load processed data into SQLite
5. Prepare data for downstream analysis

---

## Status

Project under active development.

### Completed Milestones

* Repository initialised
* Project structure implemented
* Open-Meteo API integration completed
* Weather data extraction workflow implemented
* Data cleaning and feature engineering completed
* SQLite database loading completed
* End-to-end ETL orchestration implemented (`pipeline.py`)
* Database validation completed using SQL queries

### Upcoming Enhancements

* Multi-city climate data processing
* Data quality validation checks
* Logging and monitoring
* Climate trend visualisations
* Automated reporting

