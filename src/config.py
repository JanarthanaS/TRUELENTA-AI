"""
Configuration settings for Truelenta AI.
Centralizes constants, file paths, and external API keys (simulated).
"""
import os
from pathlib import Path

# Base Paths
BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "assets"
THUMBNAIL_DIR = ASSETS_DIR / "thumbnails"
OUTPUT_DIR = ASSETS_DIR / "sample_output"
LOG_DIR = BASE_DIR / "logs"

# Ensure directories exist
for path in [THUMBNAIL_DIR, OUTPUT_DIR, LOG_DIR]:
    path.mkdir(parents=True, exist_ok=True)

# Data Sources
# In a real scenario, these would be loaded from a DB or YAML
RSS_FEEDS = [
    "https://feeds.feedburner.com/ndtvnews-top-stories",
    "https://www.thehindu.com/news/national/feeder/default.rss",
    # TODO: Add specific regional feeds for Tamil/Telugu coverage
]

TRUSTED_DOMAINS = [
    "ndtv.com",
    "ddnews.gov.in",
    "thehindu.com",
    "indianexpress.com"
]

# Classification Config
CATEGORIES = {
    "politics": ["election", "minister", "parliament", "vote", "congress", "bjp", "modi"],
    "finance": ["sensex", "nifty", "rbi", "bank", "economy", "market", "stocks"],
    "tech": ["ai", "google", "apple", "crypto", "software", "startup"],
    "sports": ["cricket", "kohli", "bcci", "olympics", "match"],
    "entertainment": ["movie", "bollywood", "actor", "cinema", "song"],
    "world": ["war", "un", "usa", "china", "treaty"]
}

# Pipeline Settings
MIN_SIMILARITY_SCORE = 0.4
MAX_RETRIES = 3