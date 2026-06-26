from pathlib import Path
from datetime import datetime

from logger import logger


def generate_run_summary(summary, output_file="outputs/reports/etl_summary.txt"):
    report_path = Path(output_file)
    report_path.parent.mkdir(parents=True, exist_ok=True)

    lines = [
        "=" * 60,
        "ETL RUN SUMMARY",
        "=" * 60,
        "",
        f"Run Status        : {summary['status']}",
        f"Cities Processed  : {summary['cities_processed']}",
        f"Rows Processed    : {summary['rows_processed']}",
        f"Rows Loaded       : {summary['rows_loaded']}",
        f"Rows per City     : {summary['rows_per_city']}",
        "",
        f"Database Table    : {summary['table_name']}",
        f"Date Range        : {summary['start_date']} to {summary['end_date']}",
        "",
        "Quality Checks",
        "-" * 20,
        f"Missing Values      : {summary['missing_values']}",
        f"Duplicate Records   : {summary['duplicate_records']}",
        f"Temperature Errors  : {summary['temperature_errors']}",
        f"Negative Rainfall   : {summary['negative_precipitation']}",
        "",
        f"Generated On      : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "=" * 60,
    ]

    report_text = "\n".join(lines)

    report_path.write_text(report_text + "\n")

    logger.info("ETL run summary generated")
    logger.info(f"Summary report saved to {report_path}")

    return report_path