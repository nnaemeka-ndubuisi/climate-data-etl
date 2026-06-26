import os
from pathlib import Path
import pandas as pd


def clean_weather_data(input_file, output_file, city_name):
    df = pd.read_csv(input_file, parse_dates=["time"])

    df = df.rename(
        columns={
            "time": "date",
            "temperature_2m_mean": "mean_temp",
            "temperature_2m_max": "max_temp",
            "temperature_2m_min": "min_temp",
            "precipitation_sum": "precipitation",
        }
    )

    df["city"] = city_name
    df["month"] = df["date"].dt.month
    df["year"] = df["date"].dt.year

    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(output_path, index=False)
    print(f"Cleaned data successfully saved to {output_path}")


if __name__ == "__main__":
    clean_weather_data(
        input_file="data/raw/hannover_weather_2024.csv",
        output_file="data/processed/hannover_weather_2024_clean.csv",
        city_name="hannover",
    )
