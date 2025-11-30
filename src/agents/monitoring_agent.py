"""
Agent responsible for tracking system health.
"""
import os
import time
from src.config import LOG_DIR
from src.utils.logger import get_logger

logger = get_logger(__name__)

class MonitoringAgent:
    
    def __init__(self):
        self.start_time = time.time()
        self.errors = 0
        self.articles_processed = 0

    def log_stats(self):
        """Prints current run statistics."""
        duration = time.time() - self.start_time
        logger.info("=== SESSION STATS ===")
        logger.info(f"Duration: {duration:.2f}s")
        logger.info(f"Processed: {self.articles_processed}")
        logger.info(f"Errors: {self.errors}")
        logger.info("=====================")

    def clean_old_logs(self, days=7):
        """Removes logs older than X days."""
        # TODO: Implement this to prevent disk bloat on the server
        pass