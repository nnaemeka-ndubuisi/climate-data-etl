# Climate Data ETL Pipeline

## Overview

This project demonstrates a configurable, end-to-end ETL (Extract, Transform, Load) pipeline for historical weather data using **Python, Pandas, SQLite, and the Open-Meteo Archive API**.

The pipeline automatically extracts daily weather observations for multiple German cities, performs data cleaning and feature engineering, stores analysis-ready datasets in both CSV and SQLite formats, and validates the resulting database using SQL queries.

The project showcases practical data engineering principles including API integration, modular software design, configuration-driven workflows, SQL database management, and reproducible ETL development using Git and GitHub.

---

## Project Goals

* Extract historical weather observations from a public API
* Automate data ingestion for multiple cities
* Clean and transform raw datasets
* Store processed data in CSV and SQLite formats
* Validate database integrity using SQL queries
* Demonstrate reproducible ETL pipeline development
* Provide a foundation for future climate analytics and reporting

---

## Technologies

* Python
* Pandas
* NumPy
* Requests
* SQLite
* Matplotlib
* Jupyter Notebook
* Git & GitHub

---

## Supported Cities

The pipeline currently processes historical daily weather observations for:

* Hannover
* Berlin
* Hamburg
* Munich
* Cologne

---

## Climate Variables

* Daily Mean Temperature
* Daily Maximum Temperature
* Daily Minimum Temperature
* Daily Precipitation

---

## Project Structure

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
│   └── figures/
│
├── src/
│   ├── config.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── validate.py
│   └── pipeline.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## ETL Architecture

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
```

The pipeline orchestrates the entire workflow automatically for every configured city.

---

## Example Workflow

Run the complete pipeline:

```bash
python3 src/pipeline.py
```

The pipeline automatically performs the following steps for every configured city:

1. Read city configuration
2. Extract historical weather observations from the Open-Meteo API
3. Store raw observations as CSV
4. Clean and transform the dataset
5. Load processed data into SQLite
6. Validate database integrity using SQL queries

---

## Output

After execution, the project generates:

### Raw Data

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

### Processed Data

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

### SQLite Database

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

## Database Validation

The validation module automatically verifies:

* Database creation
* Table existence
* Total rows loaded
* Column schema
* Date range
* Sample records

For the current configuration:

* **Cities:** 5
* **Observations per city:** 366
* **Total observations:** 1,830

---

## Completed Features

* Repository initialization
* Modular project architecture
* Open-Meteo API integration
* Multi-city weather data extraction
* Automated ETL orchestration
* Data cleaning and feature engineering
* Configuration-driven workflow
* SQLite database integration
* SQL-based database validation
* Dynamic file naming
* Reusable pipeline design

---

## Future Enhancements

* Advanced data quality checks
* Logging and monitoring
* Climate trend visualizations
* Automated summary reports
* Unit testing
* Support for additional weather variables
* PostgreSQL backend
* Docker containerization

---

## License

This project is intended for educational and portfolio purposes.
