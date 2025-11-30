"""
Agent responsible for final output serialization.
"""
import json
from typing import Dict, Any
from src.config import OUTPUT_DIR
from src.utils.logger import get_logger

logger = get_logger(__name__)

class PublisherAgent:
    
    def publish(self, article: Dict[str, Any]) -> bool:
        """
        Writes the processed article to disk as a JSON file suitable for the frontend.
        """
        # Final gate check
        if not article.get('is_verified', False):
            logger.info("Article rejected at publishing stage (Verification failed)")
            return False

        try:
            # Create a slug-like filename
            safe_title = "".join(x for x in article['title'] if x.isalnum())[:20]
            filename = f"{safe_title}_{article['category']}.json"
            save_path = OUTPUT_DIR / filename
            
            # Prepare final payload structure
            payload = {
                "meta": {
                    "source": article['source'],
                    "original_link": article['link'],
                    "score": article['verification_score']
                },
                "content": {
                    "title": article['title'],
                    "body": article.get('editorial_text', article['summary']),
                    "category": article['category'],
                    "language": article['language']
                },
                "social": article.get('social_content', {})
            }
            
            with open(save_path, 'w', encoding='utf-8') as f:
                json.dump(payload, f, indent=4, ensure_ascii=False)
                
            logger.info(f"PUBLISHED: {filename}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to publish article: {e}")
            return False