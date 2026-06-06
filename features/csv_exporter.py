import os
import csv

from datetime import datetime
from utils.logger import get_logger

logger  = get_logger()


class CSVExporter:
    """
    Exports log analysis summary into a CSV file.
    """

    def __init__(self, export_dir="exports"):
        self.export_dir = export_dir
        os.makedirs(self.export_dir, exist_ok=True)

    def export(self, summary: dict, most_common_error: dict = None):
        """
        Writes summary metrics into a CSV file.
        """

        logger.info("Starting CSV export")

        # Create unique filename per run
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_path = os.path.join(self.export_dir, f"summary_{timestamp}.csv")

        # Build rows
        rows = [
            ("metric", "value"),
            ("total_logs", summary.get("total_logs", 0)),
            ("errors", summary.get("ERROR", 0)),
            ("warnings", summary.get("WARNING", 0)),
            ("info", summary.get("INFO", 0)),
        ]

        # Add most common error if exists
        if most_common_error:
            rows.append(("most_common_error", most_common_error["error_message"]))

        # Write CSV
        try:
            with open(file_path, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerows(rows)

            logger.info(f"CSV exported successfully -> {file_path}")
            return file_path

        except Exception as e:
            logger.error(f"CSV export failed: {e}")
            return None