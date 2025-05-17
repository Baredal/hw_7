from celery import Celery
import time
from .logger import logger
from .alert_engine import generate_alert

# Initialize Celery application with Redis as both the broker and result backend
celery = Celery(
    'tasks',
    broker='redis://redis:6379/0',
    backend='redis://redis:6379/0'
)

@celery.task
def process_data(data: str) -> str:
    """
    Celery task that processes input text data.

    This function simulates data processing by:
      - Logging the received input.
      - Detecting keywords indicating potential fraud or sensitive personal information.
      - Triggering alerts based on the content.
      - Converting the input to lowercase to simulate processing.
      - Returning a processed result.

    Alerts are generated for:
      - Fraudulent content containing the word "fraud".
      - Sensitive data such as "ssn" or "password".
      - Empty input values.

    Args:
        data (str): The input text to be processed.

    Returns:
        str: A string message indicating the processed result.
    """
    logger.info(f"Task received: {data}")
    time.sleep(3)  # Simulate processing delay

    if "fraud" in data:
        generate_alert("Fraud Attempt", f"Suspicious input: {data}")
    elif any(word in data.lower() for word in ["ssn", "password"]):
        generate_alert("Personal Data", f"User sent sensitive data: {data}")
    elif not data:
        generate_alert("Incorrect Input", "Empty data received.")

    processed_data = data.lower()
    logger.info(f"Task completed: {processed_data}")
    return f"Processed: {processed_data}"
