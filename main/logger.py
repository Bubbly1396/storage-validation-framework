import logging
import os

class Log:

    @staticmethod
    def get_logger():

        os.makedirs("logs", exist_ok=True)

        logger = logging.getLogger("Storage_Framework")

        if not logger.handlers:

            logger.setLevel(logging.INFO)

            file_handler = logging.FileHandler("logs/Storage_Framework.log")

            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

            file_handler.setFormatter(formatter)

            logger.addHandler(file_handler)

        return logger


