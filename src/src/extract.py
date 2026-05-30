import requests
import pandas as pd


def get_weather_data(latitude, longitude, start_date, end_date):

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

    return pd.DataFrame(data["daily"])


if __name__ == "__main__":

    hannover_lat = 52.3759
    hannover_lon = 9.7320

    weather_df = get_weather_data(
        latitude=hannover_lat,
        longitude=hannover_lon,
        start_date="2024-01-01",
        end_date="2024-12-31"
    )

    print(weather_df.head())
