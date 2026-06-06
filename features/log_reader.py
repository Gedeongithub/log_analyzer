from utils.logger import get_logger
logger = get_logger()

class LogReader:

    def __init__(self, file_path: str):
        self.file_path = file_path

    def read(self):
        logger.info(f"Reading file: {self.file_path}")

        with open(self.file_path, "r", encoding="utf-8") as file:
            return [line.strip() for line in file if line.strip()]
