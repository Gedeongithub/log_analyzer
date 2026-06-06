from features.log_reader import LogReader
from features.log_format_detector import LogFormatDetector
from features.log_parser import LogParser
from features.level_counter import LeverCounter
from features.common_error_finder import CommonErrorFinder
from features.filter_logs import LogFilter
from datetime import datetime
from features.csv_exporter import CSVExporter
from utils.logger import get_logger




# =================================
# INPUT SECTION
# =================================

FILE_PATH = "logs_tobe_read/json_logs.log"

# ===================================
# READ LOGS SECTION
# =================================

logger = get_logger()
logger.info(f"Reading file: {FILE_PATH}")
reader = LogReader(FILE_PATH)
lines = reader.read()

# ==================================
# DETECTION & PARSING SECTION
# ================================

detector = LogFormatDetector()
parser = LogParser()
structured_logs =[]

for line in lines:
    line_type =detector.detect_line_type(line)
    parsed = parser.parse(line,line_type)
    
    if parsed:
        structured_logs.append(parsed)
print("\nSTRUCTURED LOGS SAMPLE")
print(structured_logs[:3])


# ===================================
# FILTER SECTION
# ================================

log_filter = LogFilter() 
filtered_logs = log_filter.filter(
    structured_logs,
    level=None,
    start_time=None,
    end_time=None
)

print("\nFILTERED LOGS COUNT:", len(filtered_logs))


# =====================================
# LEVLE COUNTER SECTION
# =============================

counter = LeverCounter()
counts = counter.count(structured_logs)
print("\nLEVEL SUMMARY")
print("Errors:", counts.get("ERROR", 0))
print("Warnings:", counts.get("WARNING", 0))
print("Info:", counts.get("INFO", 0))



# ==================================
# COMMON ERROR SECTION
# ===============================

error_finder = CommonErrorFinder()
common_error = error_finder.analyze(structured_logs)
print("\nMOST COMMON ERROR")
if common_error:
    print(common_error["error_message"], "-", common_error["count"])
else:
    print("No errors found")
    
# ===================================
# CSV EXPORT SECTION
# ==================================

exporter = CSVExporter()
summary = {
    "total_logs": len(structured_logs),
    "ERROR": counts.get("ERROR", 0),
    "WARNING": counts.get("WARNING", 0),
    "INFO": counts.get("INFO", 0),
}

export_path = exporter.export(summary, common_error)

print("\nCSV EXPORTED TO:")
print(export_path)

# =============== ENDING SECTION====================

logger.info("Log analysis completed successfully")
print("\nDONE")