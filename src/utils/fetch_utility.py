"""
Network wrapper to handle requests with retry logic and headers.
"""
import time
import requests
from requests.exceptions import RequestException
from typing import Optional

# Pretend to be a real browser to avoid 403s
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"

def fetch_url(url: str, retries: int = 3) -> Optional[str]:
    """
    Fetches content from a URL with exponential backoff.
    """
    headers = {"User-Agent": USER_AGENT}
    
    for attempt in range(retries):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            return response.text
        except RequestException as e:
            wait_time = 2 ** attempt
            # Keeping print here for immediate debug, logger handles the rest
            # print(f"Attempt {attempt + 1} failed for {url}: {e}")
            if attempt < retries - 1:
                time.sleep(wait_time)
            else:
                return None
    return None