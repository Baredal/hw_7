import logging
import os

# Path to the log file
LOG_FILE = 'logs/app.log'

# Ensure that the log directory exists
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

# Configure the logging system
logging.basicConfig(
    level=logging.INFO,  # Set the logging level to INFO
    format='%(asctime)s [%(levelname)s] %(message)s',  # Log message format
    handlers=[
        logging.FileHandler(LOG_FILE),   # Log to file
        logging.StreamHandler()          # Also log to console
    ]
)

# Create and export a logger instance for use across the application
logger = logging.getLogger(__name__)
