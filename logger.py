# app/logger.py
import logging

# Create a logger instance
logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)  # Set the log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)

# Create a console handler to log messages to the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)  # Log level for console output

# Create a file handler to log messages to a file (optional)
file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.INFO)  # Log level for file output

# Define the logging format (you can customize this as needed)
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Optionally, you can log messages to other places, like syslog or a remote server.
