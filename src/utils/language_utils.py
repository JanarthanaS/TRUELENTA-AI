"""
Utilities for language detection and handling.
"""
import re

def detect_language(text: str) -> str:
    """
    Heuristic-based language detection.
    Optimized for Indian context (En, Hi, Ta, Te).
    
    Args:
        text: The content string.
        
    Returns:
        str: ISO code ('en', 'hi', 'ta', 'te').
    """
    if not text:
        return "unknown"
        
    # Unicode ranges
    # Devanagari (Hindi): \u0900-\u097F
    # Tamil: \u0B80-\u0BFF
    # Telugu: \u0C00-\u0C7F
    
    if re.search(r'[\u0900-\u097F]', text):
        return "hi"
    if re.search(r'[\u0B80-\u0BFF]', text):
        return "ta"
    if re.search(r'[\u0C00-\u0C7F]', text):
        return "te"
        
    # Default to English if standard ASCII is dominant
    return "en"