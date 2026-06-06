# Log Analyzer CLI

A Python command-line application that reads and analyzes log files, providing actionable insights such as log level statistics, common failures, timestamp tracking, filtering, and CSV export.

The tool supports both plain-text logs and JSON-structured logs, making it suitable for application logs, server logs, and system monitoring use cases.

---

## Project Overview

Log files are one of the most valuable sources of information when troubleshooting software systems. However, manually reviewing thousands of log entries can be time-consuming and error-prone.

Log Analyzer CLI automates the process by:

- Reading log files line by line
- Detecting log formats automatically
- Extracting timestamps, log levels, and messages
- Counting log levels
- Identifying the most frequent error
- Filtering logs by level and time range
- Exporting analysis results to CSV

---

## Features

### 1. Log File Reading

Read and process log files efficiently line by line.

Supported input:

```text
2024-01-15 10:03:22 ERROR Database timeout
2024-01-15 10:04:01 INFO Server started
```

---

### 2. Automatic Log Format Detection

The application supports two log formats:

#### Plain Text Logs

```text
2024-01-15 10:03:22 ERROR Database timeout
```

#### JSON Logs

```json
{
  "timestamp": "2024-01-15 10:03:22",
  "level": "ERROR",
  "message": "Database timeout"
}
```

The parser automatically detects the format and extracts:

- Timestamp
- Log Level
- Message

---

### 3. Log Level Statistics

Counts the number of:

- ERROR logs
- WARNING logs
- INFO logs

Example:

```text
Errors:      45
Warnings:   102
Info:      1053
```

---

### 4. Most Common Error Detection

Identifies the error message that appears most frequently.

Example:

```text
Most frequent error:
Database timeout
```

---

### 5. Log Filtering

Filter log entries by:

#### Log Level

```bash
--level ERROR
```

#### Time Range

```bash
--from "2024-01-15 10:00:00"
--to "2024-01-15 12:00:00"
```

Filters can be combined for more precise analysis.

---

### 6. CSV Export

Export summary results into a CSV file.

Example output:

```csv
metric,value
total_logs,1200
errors,45
warnings,102
info,1053
most_common_error,Database timeout
```

---

## Project Structure

```text
log_analyzer/
│
├── app.py
│
├── logs/
│   └── logfile.log
│
├── logstoberead/
│   └── info.log
│
├── features/
│   ├── __init__.py
│   ├── log_reader.py
│   ├── log_format_detector.py
│   ├── level_counter.py
│   ├── common_error_finder.py
│   ├── filter_logs.py
│   └── csv_exporter.py
│
├── utils/
│   ├── __init__.py
│   └── logger.py
│
├── exports/
│
├── requirements.txt
│
└── README.md
```

---

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd log_analyzer
```

### Create Virtual Environment

#### Windows (Git Bash)

```bash
py -m venv .venv
source .venv/Scripts/activate
```

#### Windows (PowerShell)

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

### Analyze a Log File

```bash
python app.py -file logstoberead/info.log
```

---

### Filter by Log Level

```bash
python app.py -file logstoberead/info.log --level ERROR
```

---

### Filter by Date Range

```bash
python app.py \
-file logstoberead/info.log \
--from "2024-01-15 10:00:00" \
--to "2024-01-15 12:00:00"
```

---

### Export Summary

```bash
python app.py \
-file logstoberead/info.log \
--export exports/summary.csv
```

---

### Combined Example

```bash
python app.py \
-file logstoberead/info.log \
--level ERROR \
--from "2024-01-15 10:00:00" \
--to "2024-01-15 12:00:00" \
--export exports/summary.csv
```

---

## Sample Output

```text
====================================
          LOG ANALYSIS REPORT
====================================

Total Logs:           1200
Errors:                 45
Warnings:              102
Info:                 1053

Most Frequent Error:
Database timeout

Failure Timestamps:
10:03:22
10:07:44
10:15:01

====================================
```

---

## Logging

The application maintains its own execution log.

Location:

```text
logs/logfile.log
```

Example:

```text
2026-06-06 10:01:03 INFO Reading log file
2026-06-06 10:01:04 INFO Detecting log format
2026-06-06 10:01:05 INFO Counting log levels
2026-06-06 10:01:06 INFO Exporting summary
```

These logs help with debugging and monitoring application execution.

---

## Future Enhancements

Potential improvements include:

- Support for additional log formats
- Interactive dashboard
- HTML report generation
- Real-time log monitoring
- Graphical visualizations
- Database storage for historical analysis
- Email notifications for critical errors

---

## Technologies Used

- Python 3
- argparse
- logging
- json
- csv
- datetime
- collections

---

## Learning Objectives

This project demonstrates:

- Python file handling
- Object-oriented programming
- Command-line interface development
- Log parsing techniques
- Data filtering
- CSV generation
- Modular software design
- Error handling and logging

---

## Author

Developed as part of a Python backend and automation engineering learning portfolio project focused on building practical command-line tools using clean architecture and modular design principles.