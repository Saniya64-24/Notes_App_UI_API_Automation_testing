import logging
import os

# Create logs directory
os.makedirs("logs", exist_ok=True)

# Create logger
logger = logging.getLogger("automation_logger")

# Prevent duplicate logs
logger.propagate = False

# Set log level
logger.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter(
    "%(asctime)s [%(levelname)s] %(message)s"
)

# File Handler
file_handler = logging.FileHandler("logs/test_run.log", mode="a")
file_handler.setFormatter(formatter)

# Console Handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# Add handlers only once
if not logger.handlers:
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)