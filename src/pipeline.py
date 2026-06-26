from pathlib import Path
from extract import get_weather_data
from load import load_to_database
from transform import clean_weather_data
from validate import validate_database


def run_pipeline():
    print("--- Starting ETL Pipeline ---")

    # 1. Defining paths and ensuring base directories exist
    raw_dir = Path("data/raw")
    processed_dir = Path("data/processed")

    raw_dir.mkdir(parents=True, exist_ok=True)
    processed_dir.mkdir(parents=True, exist_ok=True)

    raw_file = raw_dir / "hannover_weather_2024.csv"
    processed_file = processed_dir / "hannover_weather_2024_clean.csv"
    database_file = Path("data/weather.db")

    # 2. EXTRACT
    print("[1/4] Extracting data from Open-Meteo API")
    weather_df = get_weather_data(
        latitude=52.3759,
        longitude=9.7320,
        start_date="2024-01-01",
        end_date="2024-12-31",
    )
    weather_df.to_csv(raw_file, index=False)
    print(f"      Raw data cached at: {raw_file}")

    # 3. TRANSFORM
    print("[2/4] Transforming data (cleaning & feature engineering)")
    clean_weather_data(input_file=str(raw_file), output_file=str(processed_file))

    # 4. LOAD
    print("[3/4] Loading data into SQLite database")
    load_to_database(
    input_file=str(processed_file),
    db_file=str(database_file)
)

    # 5. VALIDATE
    print("[4/4] Validating SQLite database")
    validate_database(
        db_file=str(database_file),
        table_name="weather_data",
    )
    print("\n--- Pipeline Completed Successfully ---")


if __name__ == "__main__":
    run_pipeline()
