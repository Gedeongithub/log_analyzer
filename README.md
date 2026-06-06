# Log Analyzer CLI

A Python command-line application that reads log files, analyzes them, and generates useful insights such as log level counts, most common errors, filtering results, and CSV exports.

---

## Overview

Log Analyzer CLI is designed to process log files in different formats and produce a clean summary of application activity.

The tool currently supports:

- Plain text logs
- JSON structured logs
- CSV file detection

The application reads log files, converts entries into a standardized structure, performs analysis, and exports results to CSV.

---

## Features

### Feature 1: Read Log Files

Reads files line-by-line from a specified path.

Supported file types:

- Plain text logs
- JSON logs
- CSV files

---

### Feature 2: Detect Log Format

Automatically detects the format of each log source.

Supported formats:

#### Plain Text

```text
2024-01-15 10:03:22 ERROR Database timeout
```

#### JSON

```json
{
  "timestamp": "2024-01-15 10:03:22",
  "level": "ERROR",
  "message": "Database timeout"
}
```

#### CSV

```csv
id,name,status
1,John,active
2,Mary,inactive
```

---

### Feature 3: Parse Logs

Converts supported log formats into a standardized structure:

```python
{
    "timestamp": datetime,
    "level": "ERROR",
    "message": "Database timeout",
    "format": "json",
    "raw": "original log line"
}
```

This ensures all analysis modules work with the same data structure regardless of source format.

---

### Feature 4: Count Log Levels

Counts occurrences of:

- ERROR
- WARNING
- INFO

Example:

```text
Errors:   45
Warnings: 102
Info:     1053
```

---

### Feature 5: Find Most Common Error

Identifies the error message that appears most frequently.

Example:

```text
Most Common Error:
Database timeout while connecting to users_db
Occurrences: 12
```

---

### Feature 6: Filter Logs

Supports filtering structured logs by:

#### Log Level

```text
ERROR
WARNING
INFO
```

#### Time Range

```text
Start Time
End Time
```

Filtering is performed after parsing and before analysis.

---

### Feature 7: Export Results to CSV

Exports analysis results into a CSV file.

Example output:

```csv
metric,value
total_logs,1200
errors,45
warnings,102
info,1053
most_common_error,Database timeout
```

Exports are automatically saved in the:

```text
exports/
```

directory.

Each execution generates a new file.

---

## Project Structure

```text
log_analyzer/
│
├── app.py
│
├── features/
│   ├── log_reader.py
│   ├── log_format_detector.py
│   ├── log_parser.py
│   ├── level_counter.py
│   ├── common_error_finder.py
│   ├── filter_logs.py
│   └── csv_exporter.py
│
├── utils/
│   └── logger.py
│
├── logs_tobe_read/
│   ├── text_logs.log
│   ├── json_logs.log
│   └── csv_logs.log
│
├── logs/
│   └── logfile_<timestamp>.log
│
├── exports/
│   └── summary_<timestamp>.csv
│
├── requirements.txt
└── README.md
```

---

## Logging

The application maintains execution logs for troubleshooting and auditing.

Characteristics:

- Automatically creates the `logs/` directory
- Generates a unique log file for every run
- Logs both console and file output
- Records errors, warnings, and execution details

Example:

```text
2026-06-06 15:06:56 INFO Reading file: logs_tobe_read/json_logs.log
2026-06-06 15:06:56 INFO Starting level counting
2026-06-06 15:06:56 INFO CSV exported successfully
```

---

## Installation

Clone the repository:

```bash
git clone (https://github.com/Gedeongithub/log_analyzer.git)
cd log_analyzer
```

Create a virtual environment:

```bash
py -m venv .venv
```

Activate it:

### Git Bash

```bash
source .venv/Scripts/activate
```

### PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

---

## Requirements

Python Version:

```text
Python 3.11+
```

Third-party dependencies:

```text
None
```

This project currently uses only Python's standard library.

---

## Running the Application

Example:

```bash
py app.py
```

---

## Current Analysis Pipeline

```text
LogReader
    ↓
LogFormatDetector
    ↓
LogParser
    ↓
LogFilter
    ↓
LevelCounter
    ↓
CommonErrorFinder
    ↓
CSVExporter
```

---

## Author

Developed as part of a Python CLI and software engineering learning project focused on:

- File processing
- Data parsing
- Log analysis
- Software architecture
- Modular Python development
