import json

class LogFormatDetector:
    """
    Detects format of log files and lines.
    """

    def detect_line_type(self, line: str):

        line = line.strip()

        # JSON
        if line.startswith("{") and line.endswith("}"):
            return "json"

        # CSV (very simple heuristic)
        if "," in line and not line.startswith("{"):
            return "csv"

        # Plain text log
        parts = line.split(" ")
        if len(parts) >= 3:
            return "text"

        return "ignore"