import logging
from pathlib import Path


def setup_logger():
    """
    Configure and return the project logger.

    Logs are written to:
        - Terminal (console)
        - outputs/logs/pipeline.log
    """

    log_dir = Path("outputs/logs")
    log_dir.mkdir(parents=True, exist_ok=True)

    log_file = log_dir / "pipeline.log"

    logger = logging.getLogger("climate_etl")

    # Prevent duplicate handlers if setup_logger() is called multiple times
    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # File handler
    file_handler = logging.FileHandler(log_file, mode="w")
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


# Create a reusable logger instance
logger = setup_logger()