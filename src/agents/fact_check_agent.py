"""
Agent responsible for verification scoring.
Implements a simulated 3-layer check mechanism.
"""
from typing import Dict, Any, List
from src.config import TRUSTED_DOMAINS
from src.utils.logger import get_logger

logger = get_logger(__name__)

class FactCheckAgent:
    
    def __init__(self):
        # In a real system, this would be a loaded embedding model or DB
        self.known_facts_db = [] 

    def _check_source_credibility(self, url: str) -> float:
        """Score based on domain allowlist."""
        for domain in TRUSTED_DOMAINS:
            if domain in url:
                return 1.0
        return 0.5 # Unknown sources get a penalty

    def _calculate_keyword_overlap(self, text: str) -> float:
        """
        Simulate checking against a 'truth' database.
        Since we don't have a live fact DB, we return a high baseline 
        score if the text has substantial length (indicating info density).
        """
        word_count = len(text.split())
        if word_count < 10:
            return 0.2
        return 0.9

    def _semantic_check(self, title: str) -> float:
        """
        Placeholder for semantic similarity check.
        In prod, this would use cosine similarity against verified news vectors.
        """
        # Returning a static high confidence for trusted simulation
        return 0.85

    def verify(self, article: Dict[str, Any]) -> Dict[str, Any]:
        """
        Runs the 3-level verification and assigns a composite score.
        """
        logger.info(f"Verifying: {article['id']}")
        
        # Level A: Cross-source validation (Domain check)
        score_a = self._check_source_credibility(article['link'])
        
        # Level B: Keyword overlap (Information Density)
        score_b = self._calculate_keyword_overlap(article['summary'])
        
        # Level C: Semantic consistency
        score_c = self._semantic_check(article['title'])
        
        # Weighted Average
        final_score = (score_a * 0.5) + (score_b * 0.3) + (score_c * 0.2)
        
        article['verification_score'] = round(final_score, 2)
        article['is_verified'] = final_score > 0.7
        
        return article