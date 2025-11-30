"""
Custom logger setup for the application.
Ensures we capture both console output and file logs for the MonitoringAgent.
"""
import logging
import sys
from src.config import LOG_DIR

def get_logger(name: str) -> logging.Logger:
    """
    Creates a configured logger instance.
    
    Args:
        name: The name of the module calling the logger.
        
    Returns:
        logging.Logger: Configured logger.
    """
    logger = logging.getLogger(name)
    
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)
        
        # Format: Time - Name - Level - Message
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        
        # Console Handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        
        # File Handler
        file_handler = logging.FileHandler(LOG_DIR / "truelenta.log")
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
        
    return logger