import logging
import os
from datetime import datetime

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR,"logfile.log")

os.makedirs(LOG_DIR,exist_ok=True)

def get_logger(name:str="log_analyzer"):
    
    """
    Creates a logger to write to a new log file per run.
    """
    
    logger = logging.getLogger(name)
    
    #duplicate handers prevention
    if logger.handlers:
        return logger
    logger.setLevel(logging.DEBUG)
    
    #create a unique log file per run
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = os.path.join(LOG_DIR,f"logfile_{timestamp}.log")
    
    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s %(name)s - %(message)s"
    )
    
    #file handler (New file each run in this case)
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    
    #console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    logger.info(f"Logger initialized ->{log_file}")
    
    return logger
