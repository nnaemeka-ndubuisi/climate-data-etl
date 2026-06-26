from pathlib import Path
import sqlite3
import pandas as pd


def validate_database(db_file, table_name="weather_data"):
    db_path = Path(db_file)

    print("\n--- SQLite Database Validation ---")

    if not db_path.exists():
        raise FileNotFoundError(f"Database file not found: {db_path}")

    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT name
            FROM sqlite_master
            WHERE type='table' AND name=?
            """,
            (table_name,),
        )

        table_exists = cursor.fetchone()

        if not table_exists:
            raise ValueError(f"Table '{table_name}' does not exist in {db_path}")

        row_count = pd.read_sql_query(
            f"SELECT COUNT(*) AS row_count FROM {table_name}",
            conn,
        )

        columns = pd.read_sql_query(
            f"PRAGMA table_info({table_name})",
            conn,
        )

        date_range = pd.read_sql_query(
            f"""
            SELECT 
                MIN(date) AS start_date,
                MAX(date) AS end_date
            FROM {table_name}
            """,
            conn,
        )

        sample_records = pd.read_sql_query(
            f"SELECT * FROM {table_name} LIMIT 5",
            conn,
        )

    print(f"Database file: {db_path}")
    print(f"Table found: {table_name}")

    print("\nRow count:")
    print(row_count)

    print("\nColumns:")
    print(columns[["name", "type"]])

    print("\nDate range:")
    print(date_range)

    print("\nSample records:")
    print(sample_records)

    print("\nValidation completed successfully.")


if __name__ == "__main__":
    validate_database(
        db_file="data/weather.db",
        table_name="weather_data",
    )