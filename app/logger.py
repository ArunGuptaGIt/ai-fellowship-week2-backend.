"""
logger.py - Central logging setup

All application code uses this logger instead of creating their own.
Everything gets logged to both the console and the 'log' file.
"""

import logging
import os

LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "log")
LOG_FORMAT = "%(asctime)s | %(levelname)-8s | %(name)-20s | %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def get_logger(name: str) -> logging.Logger:
    """Get a logger for a module.
    
    Usually you just call this with __name__ to get a logger for your module.
    """
    logger = logging.getLogger(name)

    # If this logger already has handlers, don't add more
    if logger.handlers:
        return logger

    logger.setLevel(logging.DEBUG)

    # Console output - shows INFO level and above
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter(LOG_FORMAT, datefmt=DATE_FORMAT))

    # File output - shows everything (DEBUG level and above)
    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(LOG_FORMAT, datefmt=DATE_FORMAT))

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
