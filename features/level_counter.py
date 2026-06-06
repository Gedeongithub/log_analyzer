from utils.logger import get_logger
from collections import defaultdict

logger = get_logger()

class LeverCounter:
    """
    Counts log levels from structured logs
    """
    def __init__(self):
        self.counts =defaultdict(int)
        

    def count(self,logs:list):
        """
        Accpets structred logs and count levels
        """
        logger.info("Starting level counting")
        
        for log in logs:
            level = log.get("level","INFO").upper()
            self.counts[level]+=1
            
        logger.info(f"level counting completed: {dict(self.counts)}")
        return dict(self.counts)
    
    def summary(self):
        """
        returns formatted summary
        """
        return {
            "ERROR": self.counts.get("ERROR", 0),
            "WARNING": self.counts.get("WARNING", 0),
            "INFO": self.counts.get("INFO", 0),
        }
        