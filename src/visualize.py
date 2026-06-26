from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from logger import logger


def create_visualizations(
    analysis_dir="outputs/analysis",
    output_dir="outputs/figures",
):
    analysis_path = Path(analysis_dir)
    figures_path = Path(output_dir)
    figures_path.mkdir(parents=True, exist_ok=True)

    logger.info("Starting climate data visualizations")

    # 1. Average temperature by city
    avg_temp = pd.read_csv(analysis_path / "average_temperature_by_city.csv")

    plt.figure(figsize=(8, 5))
    plt.bar(avg_temp["city"], avg_temp["avg_temperature"])
    plt.title("Average Temperature by City (2024)")
    plt.xlabel("City")
    plt.ylabel("Average temperature (°C)")
    plt.tight_layout()
    plt.savefig(figures_path / "average_temperature_by_city.png", dpi=300)
    plt.close()

    logger.info("Saved average temperature chart")

    # 2. Annual precipitation by city
    precipitation = pd.read_csv(analysis_path / "annual_precipitation_by_city.csv")

    plt.figure(figsize=(8, 5))
    plt.bar(precipitation["city"], precipitation["annual_precipitation"])
    plt.title("Annual Precipitation by City (2024)")
    plt.xlabel("City")
    plt.ylabel("Annual precipitation (mm)")
    plt.tight_layout()
    plt.savefig(figures_path / "annual_precipitation_by_city.png", dpi=300)
    plt.close()

    logger.info("Saved annual precipitation chart")

    # 3. Monthly temperature trends
    monthly = pd.read_csv(analysis_path / "monthly_climate_summary.csv")

    plt.figure(figsize=(10, 6))
    for city in monthly["city"].unique():
        city_data = monthly[monthly["city"] == city]
        plt.plot(
            city_data["month"],
            city_data["avg_temperature"],
            marker="o",
            label=city.title(),
        )

    plt.title("Monthly Average Temperature Trends (2024)")
    plt.xlabel("Month")
    plt.ylabel("Average temperature (°C)")
    plt.xticks(range(1, 13))
    plt.legend()
    plt.tight_layout()
    plt.savefig(figures_path / "monthly_temperature_trends.png", dpi=300)
    plt.close()

    logger.info("Saved monthly temperature trends chart")

    # 4. Monthly precipitation trends
    plt.figure(figsize=(10, 6))
    for city in monthly["city"].unique():
        city_data = monthly[monthly["city"] == city]
        plt.plot(
            city_data["month"],
            city_data["monthly_precipitation"],
            marker="o",
            label=city.title(),
        )

    plt.title("Monthly Precipitation Trends (2024)")
    plt.xlabel("Month")
    plt.ylabel("Monthly precipitation (mm)")
    plt.xticks(range(1, 13))
    plt.legend()
    plt.tight_layout()
    plt.savefig(figures_path / "monthly_precipitation_trends.png", dpi=300)
    plt.close()

    logger.info("Saved monthly precipitation trends chart")
    logger.info("Climate data visualizations completed successfully")


if __name__ == "__main__":
    create_visualizations()