import logging
import os


class LogGen:
    @staticmethod
    def loggen():
        # Change this to the correct path to your logs directory
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        log_path = os.path.join(project_root, 'logs', 'automation.log')
        log_dir = os.path.dirname(log_path)

        # Ensure the logs directory exists
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
            print(f"Created log directory: {log_dir}")

        print(f"Log file path: {log_path}")  # Debug print

        # Get the logger
        logger = logging.getLogger('classyclixLogger')
        logger.setLevel(logging.DEBUG)
        logger.propagate = False

        # Check if handlers are already added to avoid duplication
        if not logger.handlers:
            # Create file handler
            file_handler = logging.FileHandler(log_path)
            file_handler.setLevel(logging.DEBUG)
            file_formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
            file_handler.setFormatter(file_formatter)

            # Create stream handler
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(logging.DEBUG)
            stream_formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
            stream_handler.setFormatter(stream_formatter)

            # Add handlers to the logger
            logger.addHandler(file_handler)
            logger.addHandler(stream_handler)

        print(f"Logger configured: {logger}")  # Debug print

        return logger
