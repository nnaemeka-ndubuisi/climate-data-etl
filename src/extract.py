from pathlib import Path
import requests
import pandas as pd

from logger import logger


def get_weather_data(latitude, longitude, start_date, end_date):
    """
    Retrieve historical daily weather observations
    from the Open-Meteo Archive API.
    """

    logger.info(
        f"Requesting weather data ({start_date} to {end_date}) "
        f"for coordinates ({latitude}, {longitude})"
    )

    url = (
        "https://archive-api.open-meteo.com/v1/archive"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        f"&start_date={start_date}"
        f"&end_date={end_date}"
        "&daily=temperature_2m_mean,"
        "temperature_2m_max,"
        "temperature_2m_min,"
        "precipitation_sum"
        "&timezone=Europe/Berlin"
    )

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    weather_df = pd.DataFrame(data["daily"])

    logger.info(f"Retrieved {len(weather_df)} daily observations")

    return weather_df


if __name__ == "__main__":

    weather_df = get_weather_data(
        latitude=52.3759,
        longitude=9.7320,
        start_date="2024-01-01",
        end_date="2024-12-31",
    )

    logger.info("Preview of extracted data:")
    print(weather_df.head())

    output_dir = Path("data/raw")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / "hannover_weather_2024.csv"
    weather_df.to_csv(output_file, index=False)

    logger.info(f"Saved extracted data to {output_file}")