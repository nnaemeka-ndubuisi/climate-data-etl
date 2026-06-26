from pathlib import Path
import sqlite3
import pandas as pd

from logger import logger


def run_analysis(db_file="data/weather.db", output_dir="outputs/analysis"):
    db_path = Path(db_file)
    analysis_dir = Path(output_dir)
    analysis_dir.mkdir(parents=True, exist_ok=True)

    if not db_path.exists():
        raise FileNotFoundError(f"Database file not found: {db_path}")

    logger.info("Starting climate data analysis")

    queries = {
        "average_temperature_by_city": """
            SELECT
                city,
                ROUND(AVG(mean_temp), 2) AS avg_temperature
            FROM weather_data
            GROUP BY city
            ORDER BY avg_temperature DESC;
        """,
        "annual_precipitation_by_city": """
            SELECT
                city,
                ROUND(SUM(precipitation), 1) AS annual_precipitation
            FROM weather_data
            GROUP BY city
            ORDER BY annual_precipitation DESC;
        """,
        "warmest_days": """
            SELECT
                city,
                date,
                max_temp
            FROM weather_data
            ORDER BY max_temp DESC
            LIMIT 10;
        """,
        "coldest_days": """
            SELECT
                city,
                date,
                min_temp
            FROM weather_data
            ORDER BY min_temp ASC
            LIMIT 10;
        """,
        "monthly_climate_summary": """
            SELECT
                city,
                month,
                ROUND(AVG(mean_temp), 2) AS avg_temperature,
                ROUND(SUM(precipitation), 1) AS monthly_precipitation
            FROM weather_data
            GROUP BY city, month
            ORDER BY city, month;
        """,
    }

    results = {}

    with sqlite3.connect(db_path) as conn:
        for name, query in queries.items():
            logger.info(f"Running analysis query: {name}")

            result = pd.read_sql_query(query, conn)
            results[name] = result

            output_file = analysis_dir / f"{name}.csv"
            result.to_csv(output_file, index=False)

            logger.info(f"Saved analysis output to {output_file}")

    logger.info("Climate data analysis completed successfully")

    return results


if __name__ == "__main__":
    analysis_results = run_analysis()

    for name, df in analysis_results.items():
        print(f"\n{name}")
        print(df)