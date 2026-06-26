from pathlib import Path
import sqlite3
import pandas as pd
from logger import logger


def validate_database(db_file, table_name="weather_data"):
    db_path = Path(db_file)

    logger.info("Starting SQLite database validation")

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

    logger.info(f"Database file: {db_path}")
    logger.info(f"Table found: {table_name}")

    logger.info(f"Row count:\n{row_count}")
    logger.info(f"Columns:\n{columns[['name', 'type']]}")
    logger.info(f"Date range:\n{date_range}")
    logger.info(f"Sample records:\n{sample_records}")

    logger.info("Database validation completed successfully")

    return {
        "row_count": int(row_count.iloc[0, 0]),
        "columns": columns,
        "date_range": date_range,
        "sample_records": sample_records,
    }


if __name__ == "__main__":
    validate_database(
        db_file="data/weather.db",
        table_name="weather_data",
    )