import pandas as pd
from logger import logger


def run_quality_checks(input_file, expected_rows=None):
    df = pd.read_csv(input_file, parse_dates=["date"])

    logger.info("Running data quality checks")

    # 1. Missing values
    missing_values = df.isnull().sum()
    if missing_values.sum() > 0:
        logger.warning(f"Missing values found:\n{missing_values[missing_values > 0]}")
    else:
        logger.info("No missing values found")

    # 2. Duplicate city-date records
    duplicate_count = df.duplicated(subset=["city", "date"]).sum()
    if duplicate_count > 0:
        logger.warning(f"Duplicate city-date records found: {duplicate_count}")
    else:
        logger.info("No duplicate city-date records found")

    # 3. Temperature consistency
    invalid_temp_order = df[
        (df["max_temp"] < df["mean_temp"]) |
        (df["mean_temp"] < df["min_temp"])
    ]

    if len(invalid_temp_order) > 0:
        logger.warning(f"Invalid temperature ordering found: {len(invalid_temp_order)} records")
    else:
        logger.info("Temperature ordering checks passed")

    # 4. Negative precipitation
    negative_precip = df[df["precipitation"] < 0]

    if len(negative_precip) > 0:
        logger.warning(f"Negative precipitation values found: {len(negative_precip)} records")
    else:
        logger.info("Precipitation checks passed")

    # 5. Expected row count
    if expected_rows is not None:
        if len(df) != expected_rows:
            logger.warning(
                f"Unexpected row count: expected {expected_rows}, found {len(df)}"
            )
        else:
            logger.info(f"Expected row count confirmed: {expected_rows}")

    logger.info("Data quality checks completed")