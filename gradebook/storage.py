"""Handles loading and saving gradebook data using JSON."""

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
    Load data from JSON file.
    Returns a dictionary with students, courses, and enrollments.
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
    Save data to JSON file.
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
