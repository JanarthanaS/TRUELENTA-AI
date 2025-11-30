"""
Utilities for sanitizing and normalizing text data extracted from web sources.
"""
import re
import html

def clean_html(raw_html: str) -> str:
    """Removes HTML tags and decodes entities."""
    if not raw_html:
        return ""
    
    # Decode HTML entities first (&amp; -> &)
    text = html.unescape(raw_html)
    
    # Remove generic tags
    cleanr = re.compile('<.*?>')
    text = re.sub(cleanr, '', text)
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def normalize_title(title: str) -> str:
    """Normalizes titles for comparison (lowercase, remove punctuation)."""
    if not title:
        return ""
    
    # Keep only alphanumeric and spaces
    # TODO: This might strip non-English chars too aggressively. 
    # Need to check Unicode ranges for Hindi/Tamil later.
    text = re.sub(r'[^\w\s]', '', title, flags=re.UNICODE)
    return text.lower().strip()

def truncate_text(text: str, max_chars: int = 200) -> str:
    """Helper to cut text cleanly."""
    if len(text) <= max_chars:
        return text
    return text[:max_chars].rsplit(' ', 1)[0] + "..."