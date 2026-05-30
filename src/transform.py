import pandas as pd


def clean_weather_data(input_file, output_file):

    df = pd.read_csv(input_file)

    df["time"] = pd.to_datetime(df["time"])

    df.columns = [
        "date",
        "mean_temp",
        "max_temp",
        "min_temp",
        "precipitation"
    ]

    df["month"] = df["date"].dt.month
    df["year"] = df["date"].dt.year

    df.to_csv(output_file, index=False)

    print(f"Cleaned data saved to {output_file}")


if __name__ == "__main__":

    clean_weather_data(
        input_file="data/raw/hannover_weather_2024.csv",
        output_file="data/processed/hannover_weather_2024_clean.csv"
    )

