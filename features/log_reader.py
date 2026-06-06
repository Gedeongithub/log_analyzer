import json
from datetime import datetime
from utils.logger import get_logger

logger = get_logger()


class LogReader:
    """
    In charge of readin' raw log files and convert 'em into
    structure log obj
    """
    def __int__(self,file_path:str):
        self.file_path = file_path
        self.logs = []
        
    def read(self):
        """
        reads file line by line and parses each entry
        """
        logger.info(f"Reading log file: {self.file_path}")
        
        try:
            with open(self.file_path,"r",encoding="utf-8") as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    
                    parsed = self._parse_line(line)
                    
                    if parsed:
                        self.logs.append(parsed)
                        
            logger.info(f"Finished readin' logs. Total entries: {len(self.logs)}")
            return self.logs
        
        except Exception as e:
            logger.error(f"Failed to read log file: {e}")
            return []
        
    def _parse_line(self,line:str):
        """
        Detects format & parses a signgle log line.
        Supports: Plain text logs & JSON logs
        """
        
        #reads JSON format first
        try:
            data = json.loads(line)
            return {
                "timestamp":self._parse_time(data.get("timestamp")),
                "level":data.get("level","INFO"),
                "message":data.get("message",""),
                "raw":line,
                "format":"json"
            }
            
        except json.JSONDecodeError:
            pass
        
        #----------------------------------------
        #fallback: plain text
        #Format: YYY-MM-DD-HH:MM:SS LEVEL MESSAGE
        #----------------------------------------
        
        try:
            parts = line.split(" ",3)
            
            timestamp_str = f"{parts[0]} {parts[1]}"
            level = parts[2]
            message = parts[3] if len(parts)>3 else ""
            
            return {
                "timestamp":self._parse_time(timestamp_str),
                "level":level,
                "message":message,
                "raw":line,
                "format":"text"
            }
            
        except Exception as e:
            logger.warning(f"could not parse line: {line} | Error: {e}")
            return None
        
    def _parse_time(self,time_str:str):
        
        """
        Converts timestamp string into datetime object.
        """
        try:
            return datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
        except Exception:
            return None
    