from logger import logger
from pathlib import Path
from extract import get_weather_data
from load import load_to_database
from quality import run_quality_checks
from transform import clean_weather_data
from validate import validate_database
from config import CITIES, START_DATE, END_DATE, YEAR


def run_pipeline():
    logger.info("--- Starting Multi-City ETL Pipeline ---")

    raw_dir = Path("data/raw")
    processed_dir = Path("data/processed")
    raw_dir.mkdir(parents=True, exist_ok=True)
    processed_dir.mkdir(parents=True, exist_ok=True)

    database_file = Path("data/weather.db")

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
        logger.info(f"      Raw data cached at: {raw_file}")

        logger.info("[2/4] Transforming data")
        clean_weather_data(
            input_file=str(raw_file),
            output_file=str(processed_file),
            city_name=city_key,
        )
        run_quality_checks(
            input_file=str(processed_file),
            expected_rows=366,
        )

        logger.info("[3/4] Loading data into SQLite database")
        load_mode = "replace" if index == 0 else "append"
        load_to_database(
            input_file=str(processed_file),
            db_file=str(database_file),
            if_exists=load_mode,
        )

    logger.info("=" * 60)
    logger.info("[4/4] Validating SQLite database")
    validate_database(
        db_file=str(database_file),
        table_name="weather_data",
    )

    logger.info("=" * 60)
    logger.info("Multi-City ETL Pipeline completed successfully.")


if __name__ == "__main__":
    run_pipeline()
    
