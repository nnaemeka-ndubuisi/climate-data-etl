import pandas as pd
from logger import logger


def run_quality_checks(input_file, expected_rows=None):
    df = pd.read_csv(input_file, parse_dates=["date"])

    logger.info("Running data quality checks")

    # -------------------------------------------------
    # 1. Missing values
    # -------------------------------------------------
    missing_values = int(df.isnull().sum().sum())

    if missing_values > 0:
        logger.warning(f"Missing values found: {missing_values}")
    else:
        logger.info("No missing values found")

    # -------------------------------------------------
    # 2. Duplicate city-date records
    # -------------------------------------------------
    duplicate_records = int(df.duplicated(subset=["city", "date"]).sum())

    if duplicate_records > 0:
        logger.warning(f"Duplicate city-date records found: {duplicate_records}")
    else:
        logger.info("No duplicate city-date records found")

    # -------------------------------------------------
    # 3. Temperature consistency
    # -------------------------------------------------
    temperature_errors = int(
        (
            (df["max_temp"] < df["mean_temp"]) |
            (df["mean_temp"] < df["min_temp"])
        ).sum()
    )

    if temperature_errors > 0:
        logger.warning(
            f"Invalid temperature ordering found: {temperature_errors} records"
        )
    else:
        logger.info("Temperature ordering checks passed")

    # -------------------------------------------------
    # 4. Negative precipitation
    # -------------------------------------------------
    negative_precipitation = int((df["precipitation"] < 0).sum())

    if negative_precipitation > 0:
        logger.warning(
            f"Negative precipitation values found: {negative_precipitation} records"
        )
    else:
        logger.info("Precipitation checks passed")

    # -------------------------------------------------
    # 5. Expected row count
    # -------------------------------------------------
    row_count = len(df)

    if expected_rows is not None:
        if row_count != expected_rows:
            logger.warning(
                f"Unexpected row count: expected {expected_rows}, found {row_count}"
            )
        else:
            logger.info(f"Expected row count confirmed: {expected_rows}")

    logger.info("Data quality checks completed")

    # -------------------------------------------------
    # Return quality metrics for reporting
    # -------------------------------------------------
    return {
        "missing_values": missing_values,
        "duplicate_records": duplicate_records,
        "temperature_errors": temperature_errors,
        "negative_precipitation": negative_precipitation,
        "row_count": row_count,
    }


if __name__ == "__main__":
    summary = run_quality_checks(
        input_file="data/processed/hannover_weather_2024_clean.csv",
        expected_rows=366,
    )

    print(summary)