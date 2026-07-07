"""
logger.py
Professional logging module for System Information Gatherer
"""

import logging
from pathlib import Path

from config import LOG_DIR, LOG_FILE


class Logger:

    @staticmethod
    def setup():

        # Create log directory
        Path(LOG_DIR).mkdir(parents=True, exist_ok=True)

        logger = logging.getLogger("SystemInformationGatherer")
        logger.setLevel(logging.INFO)

        # Prevent duplicate logs
        if logger.hasHandlers():
            logger.handlers.clear()

        # File Handler
        file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
        file_handler.setLevel(logging.INFO)

        # Console Handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Formatter
        formatter = logging.Formatter(
            "[%(asctime)s] %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        return logger