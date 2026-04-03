"""Module for loading and saving gradebook data using JSON files.

Provides functions to persist and retrieve students, courses, and enrollments.
Handles missing or corrupted files and logs operations to `logs/app.log`.
"""

import json
import logging
from pathlib import Path

# Default data file path
DATA_PATH = Path("data/gradebook.json")

# Configure logging
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def load_data():
    """
    Load gradebook data from the JSON file.

    Returns:
        dict: Dictionary containing keys 'students', 'courses', 'enrollments'.

    Notes:
        - If the file does not exist, returns empty data.
        - If the JSON is corrupted, prints a warning and returns empty data.
        - Any unexpected exception is logged and empty data is returned.
    """
    EMPTY_DATA = {
        "students": [],
        "courses": [],
        "enrollments": []
    }
    try:
        with open(DATA_PATH, "r") as file:
            data = json.load(file)
            logging.info("Data loaded successfully")
            return data

    except FileNotFoundError:
        logging.warning("Data file not found. Starting with empty data.")
        return EMPTY_DATA.copy()

    except json.JSONDecodeError:
        logging.error("JSON file is corrupted. Starting with empty data.")
        print("Warning: The gradebook file is corrupted. Starting with a fresh record.")
        return EMPTY_DATA.copy()

    except Exception as e:
        logging.error(f"Unexpected error while loading data: {e}")
        print("Error loading data.")
        return EMPTY_DATA.copy()


def save_data(data):
    """
    Save gradebook data to the JSON file.

    Args:
        data (dict): Dictionary containing 'students', 'courses', and 'enrollments' to save.

    Notes:
        - Creates the data directory if it does not exist.
        - Logs success or any exceptions encountered.
    """
    try:
        # Ensure directory exists
        DATA_PATH.parent.mkdir(parents=True, exist_ok=True)

        with open(DATA_PATH, "w") as file:
            json.dump(data, file, indent=4)

        logging.info("Data saved successfully")

    except Exception as e:
        logging.error(f"Error saving data: {e}")
        print("Error saving data.")
