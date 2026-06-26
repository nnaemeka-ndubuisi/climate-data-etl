import sqlite3
from pathlib import Path
import pandas as pd
from logger import logger


def load_to_database(input_file, db_file, if_exists="replace"):
    df = pd.read_csv(input_file)

    db_path = Path(db_file)
    db_path.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(db_path) as conn:
        df.to_sql(
            name="weather_data",
            con=conn,
            if_exists=if_exists,
            index=False,
        )

    logger.info(f"Data successfully loaded into database: {db_path}")


if __name__ == "__main__":
    load_to_database(
        input_file="data/processed/hannover_weather_2024_clean.csv",
        db_file="data/weather.db",
        if_exists="replace",
    )