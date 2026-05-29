# Climate Data ETL Pipeline

## Overview

This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline for historical climate data across major German cities.

The objective is to automate the collection, cleaning, storage, and analysis of weather observations using Python and open climate datasets.

The project is designed to show practical environmental data science, data engineering, and analytics skills through a reproducible workflow.

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

## Cities Included

- Hannover
- Berlin
- Hamburg
- Munich
- Cologne

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

## Status

Project under active development.

Current milestone:
- Repository initialised
- Project structure design completed

Next milestone:
- Weather data extraction from Open-Meteo API
