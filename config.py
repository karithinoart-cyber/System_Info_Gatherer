"""
config.py
Configuration file for System Information Gatherer
"""

from pathlib import Path

# Project Information
PROJECT_NAME = "System Information Gatherer"
VERSION = "2.0"
AUTHOR = "I.P SINGH"

# Base Directory
BASE_DIR = Path(__file__).resolve().parent

# Reports Directory
REPORT_DIR = BASE_DIR / "reports"

# Logs Directory
LOG_DIR = BASE_DIR / "logs"

# Report Formats
REPORT_FORMATS = [
    "json",
    "txt",
    "html"
]

# Logging
LOG_FILE = LOG_DIR / "app.log"

# Network Settings
PUBLIC_IP_API = "https://api.ipify.org?format=json"

# Console
LINE = "=" * 70
SMALL_LINE = "-" * 70

# Timeout (seconds)
REQUEST_TIMEOUT = 5