from pathlib import Path
import sqlite3

import matplotlib.pyplot as plt
import pandas as pd

from logger import logger


def load_weather_data(db_file="data/weather.db"):
    db_path = Path(db_file)

    if not db_path.exists():
        raise FileNotFoundError(f"Database file not found: {db_path}")

    with sqlite3.connect(db_path) as conn:
        df = pd.read_sql_query(
            "SELECT * FROM weather_data",
            conn,
            parse_dates=["date"],
        )

    return df


def plot_average_temperature(analysis_path, figures_path):
    avg_temp = pd.read_csv(analysis_path / "average_temperature_by_city.csv")

    plt.figure(figsize=(8, 5))
    plt.bar(avg_temp["city"].str.title(), avg_temp["avg_temperature"])
    plt.title("Average Temperature by City (2024)")
    plt.xlabel("City")
    plt.ylabel("Average temperature (°C)")
    plt.tight_layout()
    plt.savefig(figures_path / "average_temperature_by_city.png", dpi=300)
    plt.close()

    logger.info("Saved average temperature bar chart")


def plot_annual_precipitation(analysis_path, figures_path):
    precipitation = pd.read_csv(analysis_path / "annual_precipitation_by_city.csv")

    plt.figure(figsize=(8, 5))
    plt.bar(
        precipitation["city"].str.title(),
        precipitation["annual_precipitation"],
    )
    plt.title("Annual Precipitation by City (2024)")
    plt.xlabel("City")
    plt.ylabel("Annual precipitation (mm)")
    plt.tight_layout()
    plt.savefig(figures_path / "annual_precipitation_by_city.png", dpi=300)
    plt.close()

    logger.info("Saved annual precipitation bar chart")


def plot_monthly_climate_dynamics(analysis_path, figures_path):
    monthly = pd.read_csv(analysis_path / "monthly_climate_summary.csv")

    cities = monthly["city"].unique()

    fig, axes = plt.subplots(
        nrows=len(cities),
        ncols=1,
        figsize=(10, 14),
        sharex=True,
    )

    for ax, city in zip(axes, cities):
        city_data = monthly[monthly["city"] == city]

        ax.bar(
            city_data["month"],
            city_data["monthly_precipitation"],
            alpha=0.6,
            label="Precipitation",
        )

        ax.set_ylabel("Precip. (mm)")
        ax.set_title(city.title())

        temp_ax = ax.twinx()
        temp_ax.plot(
            city_data["month"],
            city_data["avg_temperature"],
            marker="o",
            linewidth=2,
            label="Temperature",
        )
        temp_ax.set_ylabel("Temp. (°C)")

    axes[-1].set_xlabel("Month")
    axes[-1].set_xticks(range(1, 13))

    fig.suptitle("Monthly Climate Dynamics by City (2024)", fontsize=14)
    fig.tight_layout(rect=[0, 0, 1, 0.97])

    plt.savefig(figures_path / "monthly_climate_dynamics.png", dpi=300)
    plt.close()

    logger.info("Saved monthly climate dynamics chart")


def plot_temperature_profiles(df, figures_path):
    cities = sorted(df["city"].unique())

    fig, axes = plt.subplots(
        nrows=1,
        ncols=3,
        figsize=(16, 6),
        sharey=True,
    )

    temperature_columns = [
        ("mean_temp", "Mean Temperature"),
        ("max_temp", "Maximum Temperature"),
        ("min_temp", "Minimum Temperature"),
    ]

    for ax, (column, title) in zip(axes, temperature_columns):
        data = [df[df["city"] == city][column] for city in cities]

        ax.boxplot(data, labels=[city.title() for city in cities])
        ax.set_title(title)
        ax.set_xlabel("City")
        ax.tick_params(axis="x", rotation=30)

    axes[0].set_ylabel("Temperature (°C)")

    fig.suptitle("Temperature Profiles and Volatility by City (2024)", fontsize=14)
    fig.tight_layout(rect=[0, 0, 1, 0.94])

    plt.savefig(figures_path / "temperature_profiles_boxplot.png", dpi=300)
    plt.close()

    logger.info("Saved temperature profiles box plot")


def plot_rainfall_distribution(df, figures_path):
    rainy_days = df[df["precipitation"] > 0]
    cities = sorted(rainy_days["city"].unique())

    data = [rainy_days[rainy_days["city"] == city]["precipitation"] for city in cities]

    plt.figure(figsize=(10, 6))
    plt.boxplot(data, labels=[city.title() for city in cities])
    plt.title("Heavy Rainfall Distribution by City (Rainy Days Only, 2024)")
    plt.xlabel("City")
    plt.ylabel("Daily precipitation on rainy days (mm)")
    plt.xticks(rotation=30)
    plt.tight_layout()

    plt.savefig(figures_path / "rainfall_distribution_boxplot.png", dpi=300)
    plt.close()

    logger.info("Saved rainfall distribution box plot")


def create_visualizations(
    analysis_dir="outputs/analysis",
    output_dir="outputs/figures",
    db_file="data/weather.db",
):
    analysis_path = Path(analysis_dir)
    figures_path = Path(output_dir)
    figures_path.mkdir(parents=True, exist_ok=True)

    logger.info("Starting climate data visualizations")

    weather_df = load_weather_data(db_file)

    plot_average_temperature(analysis_path, figures_path)
    plot_annual_precipitation(analysis_path, figures_path)
    plot_monthly_climate_dynamics(analysis_path, figures_path)
    plot_temperature_profiles(weather_df, figures_path)
    plot_rainfall_distribution(weather_df, figures_path)

    logger.info("Climate data visualizations completed successfully")


if __name__ == "__main__":
    create_visualizations()