from collections import defaultdict
from utils.logger import get_logger

logger = get_logger()


class CommonErrorFinder:
    """
    Finds the most common error message in structured logs.
    """
    def __init__(self):
        self.error_counts = defaultdict(int)

    def analyze(self, logs: list):
        """
        Extract ERROR logs and count message frequency.
        """
        logger.info("Analyzing common errors")

        for log in logs:
            level = log.get("level", "").upper()
            message = log.get("message", "")

            if level == "ERROR" and message:
                self.error_counts[message] += 1

        logger.info(f"Error frequency map: {dict(self.error_counts)}")

        return self.get_most_common_error()

    def get_most_common_error(self):
        """
        Returns the most frequent error message.
        """
        if not self.error_counts:
            return None

        most_common = max(self.error_counts.items(), key=lambda x: x[1])

        return {
            "error_message": most_common[0],
            "count": most_common[1]
        }