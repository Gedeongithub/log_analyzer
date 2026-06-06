import json
from datetime import datetime
from utils.logger import get_logger

logger = get_logger()

class LogParser:
    """
    Converts raw log lines into structured  log objects.
    it works with, json and plain texts logs
    """
    
    def parse(self,line:str,line_type:str):
        """
        This is the main entry point for parsing
        """
        if line_type =="json":
            return self._parse_json(line)
        
        if line_type =="text":
            return self._parse_text(line)
        
        #CSV or other formats are ignored
        logger.info(f"Skipping unsupported line type: {line_type}")
        return None
    
    
    # JSON PARSER
    # --------------------------
    def _parse_json(self, line: str):
        try:
            data = json.loads(line)

            return {
                "timestamp": self._parse_time(data.get("timestamp")),
                "level": data.get("level", "INFO"),
                "message": data.get("message", ""),
                "format": "json",
                "raw": line
            }

        except Exception as e:
            logger.warning(f"Failed to parse JSON line: {line} | {e}")
            return None


    # TEXT PARSER
    # --------------------------
    def _parse_text(self, line: str):
        try:
            parts = line.split(" ", 3)

            if len(parts) < 3:
                return None

            timestamp_str = f"{parts[0]} {parts[1]}"
            level = parts[2]
            message = parts[3] if len(parts) > 3 else ""

            return {
                "timestamp": self._parse_time(timestamp_str),
                "level": level,
                "message": message,
                "format": "text",
                "raw": line
            }

        except Exception as e:
            logger.warning(f"Failed to parse text line: {line} | {e}")
            return None

    # TIME PARSER
    # --------------------------
    def _parse_time(self, time_str: str):
        try:
            return datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
        except Exception:
            return None
    
        
    