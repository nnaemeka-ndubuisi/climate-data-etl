from pathlib import Path

from config import CITIES, START_DATE, END_DATE, YEAR
from extract import get_weather_data
from load import load_to_database
from logger import logger
from quality import run_quality_checks
from report import generate_run_summary
from transform import clean_weather_data
from validate import validate_database


def run_pipeline():
    logger.info("--- Starting Multi-City ETL Pipeline ---")

    raw_dir = Path("data/raw")
    processed_dir = Path("data/processed")
    raw_dir.mkdir(parents=True, exist_ok=True)
    processed_dir.mkdir(parents=True, exist_ok=True)

    database_file = Path("data/weather.db")

    total_rows_processed = 0
    quality_summary = {
        "missing_values": 0,
        "duplicate_records": 0,
        "temperature_errors": 0,
        "negative_precipitation": 0,
    }

    for index, (city_key, city) in enumerate(CITIES.items()):
        logger.info("=" * 60)
        logger.info(f"Processing city: {city_key.title()}")

        raw_file = raw_dir / f"{city_key}_weather_{YEAR}.csv"
        processed_file = processed_dir / f"{city_key}_weather_{YEAR}_clean.csv"

        logger.info("[1/4] Extracting data from Open-Meteo API")
        weather_df = get_weather_data(
            latitude=city["latitude"],
            longitude=city["longitude"],
            start_date=START_DATE,
            end_date=END_DATE,
        )
        weather_df.to_csv(raw_file, index=False)
        logger.info(f"Raw data cached at: {raw_file}")

        logger.info("[2/4] Transforming data")
        clean_weather_data(
            input_file=str(raw_file),
            output_file=str(processed_file),
            city_name=city_key,
        )

        quality = run_quality_checks(
            input_file=str(processed_file),
            expected_rows=366,
        )

        total_rows_processed += quality["row_count"]
        quality_summary["missing_values"] += quality["missing_values"]
        quality_summary["duplicate_records"] += quality["duplicate_records"]
        quality_summary["temperature_errors"] += quality["temperature_errors"]
        quality_summary["negative_precipitation"] += quality["negative_precipitation"]

        logger.info("[3/4] Loading data into SQLite database")
        load_mode = "replace" if index == 0 else "append"
        load_to_database(
            input_file=str(processed_file),
            db_file=str(database_file),
            if_exists=load_mode,
        )

    logger.info("=" * 60)
    logger.info("[4/4] Validating SQLite database")
    validation = validate_database(
        db_file=str(database_file),
        table_name="weather_data",
    )

    summary = {
        "status": "SUCCESS",
        "cities_processed": len(CITIES),
        "rows_processed": total_rows_processed,
        "rows_loaded": validation["row_count"],
        "rows_per_city": total_rows_processed // len(CITIES),
        "table_name": "weather_data",
        "start_date": validation["date_range"].iloc[0]["start_date"],
        "end_date": validation["date_range"].iloc[0]["end_date"],
        "missing_values": quality_summary["missing_values"],
        "duplicate_records": quality_summary["duplicate_records"],
        "temperature_errors": quality_summary["temperature_errors"],
        "negative_precipitation": quality_summary["negative_precipitation"],
    }

    generate_run_summary(summary)

    logger.info("=" * 60)
    logger.info("Multi-City ETL Pipeline completed successfully.")


if __name__ == "__main__":
    run_pipeline()