"""
Agent responsible for ingesting raw data from configured RSS feeds.
"""
import feedparser # type: ignore
import requests
from datetime import datetime
from typing import List, Dict, Any
from src.config import RSS_FEEDS
from src.utils.logger import get_logger
from src.utils.text_cleaner import clean_html

logger = get_logger(__name__)

# Some servers block non-browser-like requests. We send a standard header package
# to make our script's request look more like it's from a real browser.
REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
}

class SourceCollectorAgent:
    """Fetches and normalizes news items."""
    
    def __init__(self):
        self.seen_urls = set()

    def collect_news(self) -> List[Dict[str, Any]]:
        """
        Iterates through RSS feeds and aggregates news items.
        
        Returns:
            List of raw article dictionaries.
        """
        raw_articles = []
        
        for feed_url in RSS_FEEDS:
            logger.info(f"Fetching feed: {feed_url}")
            
            try:
                # Use requests library for more robust fetching, as it handles modern TLS/SSL better.
                response = requests.get(feed_url, headers=REQUEST_HEADERS, timeout=15)
                response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
                
                # Pass the downloaded content to feedparser
                feed = feedparser.parse(response.content)

            except requests.exceptions.RequestException as e:
                logger.error(f"Failed to fetch feed {feed_url}. Error: {e}")
                continue # Skip to the next feed
            
            if feed.bozo:
                logger.warning(f"Malformed feed data from {feed_url}. Reason: {feed.bozo_exception}")
                continue

            for entry in feed.entries:
                link = entry.get('link', '')
                
                # Basic deduplication
                if link in self.seen_urls:
                    continue
                
                self.seen_urls.add(link)
                
                # Extract and clean
                article = {
                    'id': link, # Use URL as ID for now
                    'title': clean_html(entry.get('title', '')),
                    'summary': clean_html(entry.get('summary', '')),
                    'link': link,
                    'published_at': entry.get('published', datetime.now().isoformat()),
                    'source': feed.feed.get('title', 'Unknown Source'),
                    'raw_content': entry # store full object just in case
                }
                
                raw_articles.append(article)
        
        logger.info(f"Collected {len(raw_articles)} unique articles.")
        return raw_articles

# For manual testing
if __name__ == "__main__":
    agent = SourceCollectorAgent()
    items = agent.collect_news()
    print(f"Got {len(items)} items")