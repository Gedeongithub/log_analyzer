from datetime import datetime
from utils.logger import get_logger

logger = get_logger()


class LogFilter:
    """
    Filters structured logs by level and time range.
    """
    def __init__(self):
        pass

    def filter(self, logs: list, level=None, start_time=None, end_time=None):
        """
        Apply filtering rules to logs.
        """
        logger.info("Starting log filtering")

        filtered_logs = []

        for log in logs:
            log_level = log.get("level", "").upper()
            timestamp = log.get("timestamp")

       
            # LEVEL FILTER
            # -----------------------
            if level and log_level != level.upper():
                continue

         
            # TIME FILTER
            # -----------------------
            if timestamp:
                if start_time and timestamp < start_time:
                    continue

                if end_time and timestamp > end_time:
                    continue

            filtered_logs.append(log)

        logger.info(f"Filtering completed. {len(filtered_logs)} logs passed filter")
        return filtered_logs