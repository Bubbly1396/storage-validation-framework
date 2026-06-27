import logging

class Log:

    @staticmethod
    def get_logger():
        
        logger = logging.getLogger()
        
        logger.setLevel(logging.INFO)
        
        handler = logging.FileHandler("logs/framework.log")
        
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        
        handler.setFormatter(formatter)
        
        logger.addHandler(handler)
        
        return logger