"""
Agent responsible for taxonomy and language detection.
"""
from typing import Dict, Any
from src.config import CATEGORIES
from src.utils.language_utils import detect_language
from src.utils.logger import get_logger

logger = get_logger(__name__)

class ClassifierAgent:
    
    def process(self, article: Dict[str, Any]) -> Dict[str, Any]:
        """
        Augments the article with 'category' and 'language' fields.
        """
        text_content = (article['title'] + " " + article['summary']).lower()
        
        # 1. Detect Language
        lang = detect_language(text_content)
        article['language'] = lang
        
        # 2. Categorize
        # Start with 'general' as default
        assigned_category = "general"
        
        # Simple keyword matching
        # TODO: Replace with a BERT classifier if we get GPU budget later.
        max_hits = 0
        
        for category, keywords in CATEGORIES.items():
            hits = sum(1 for kw in keywords if kw in text_content)
            if hits > max_hits:
                max_hits = hits
                assigned_category = category
        
        article['category'] = assigned_category
        
        # 3. Regional Relevance (Heuristic)
        # If language is Tamil/Telugu/Hindi, it likely has specific regional relevance
        if lang in ['ta', 'te']:
            article['is_regional_focus'] = True
        else:
            article['is_regional_focus'] = False
            
        logger.debug(f"Classified '{article['title'][:30]}...' as {assigned_category} [{lang}]")
        return article