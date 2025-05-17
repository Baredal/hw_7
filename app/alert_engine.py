import os
from datetime import datetime

# Directory to store alert reports
ALERT_DIR = 'error_reports'
os.makedirs(ALERT_DIR, exist_ok=True)

def generate_alert(alert_type: str, description: str):
    """
    Generate an alert by writing a report to a timestamped file.

    Args:
        alert_type (str): A short type/category for the alert (e.g., "Fraud Attempt").
        description (str): A detailed message describing the alert.

    The alert file will be saved under the ALERT_DIR with a timestamped filename,
    making it easy to track and inspect issues over time.
    """
    # Generate a timestamp and sanitize it for filenames
    timestamp = datetime.now().isoformat()
    filename = f"{ALERT_DIR}/{timestamp.replace(':', '_')}_{alert_type}.txt"
    
    # Write alert details to the file
    with open(filename, 'w') as f:
        f.write(f"Time: {timestamp}\n")
        f.write(f"Alert Type: {alert_type}\n")
        f.write(f"Description: {description}\n")
