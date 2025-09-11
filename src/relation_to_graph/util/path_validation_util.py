import os
import tempfile
import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

def valid_config_file(file_path: str) -> bool:
    """
    Validates whether the specified configuration file exists and is readable.

    Args:
        file_path (str): The path to the configuration file to validate.

    Returns:
        int: Returns True if the file exists and is readable, otherwise returns False.

    Logs:
        Logs an info message if the file exists and is readable.
        Logs an error message if the file does not exist or is not readable.
    """

    if os.path.isfile(file_path) and os.access(file_path, os.R_OK):
        logging.info(f"The file '{file_path}' exists and is readable.")
        return True
    else:
        logging.error(f"The file '{file_path}' does not exist or is not readable.")
        return False


def valid_output_directory(file_path: str) ->bool:
    """
    Checks if the specified directory has write permissions.

    Args:
        directory_path (str): The path to the directory to check.

    Returns:
        bool: True if write permissions are granted, False otherwise.
    """
    directory_path = os.path.dirname(file_path)
    logging.info(f"The directory of '{file_path}' is: {directory_path}")
    
    if os.access(directory_path, os.W_OK):
        logging.info(f"Write permissions are granted for: {directory_path}")
        return True
    else:
        print(f"Write permissions are NOT granted for: {directory_path}")
        return False

def can_create_directory(path):
    """
    Checks if the user has permission to create a directory at the given path.

    Args:
        path (str): The path where the directory creation permission is to be checked.

    Returns:
        bool: True if the user can create a directory at the path, False otherwise.
    """
    try:
        # Create a temporary directory within the specified path
        temp_dir_path = tempfile.mkdtemp(dir=path)
        # Remove the temporary directory
        os.rmdir(temp_dir_path)
        return True
    except OSError:
        # An OSError indicates a permission issue or other file system error
        return False
    except Exception as e:
        # Catch any other unexpected errors
        logging.error(f"An unexpected error occurred: {e}")
        return False
