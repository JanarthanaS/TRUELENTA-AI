"""
Agent responsible for media asset generation metadata.
(Note: Actual image generation via PIL is mocked here to keep dependencies light,
but logic for file management is real).
"""
import uuid
import json
from typing import Dict, Any
from src.config import THUMBNAIL_DIR
from src.utils.logger import get_logger

logger = get_logger(__name__)

class MediaAgent:
    
    def generate_assets(self, article: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates metadata for thumbnails.
        """
        if not article.get('is_verified', False):
            return article

        # Generate unique filename
        file_id = str(uuid.uuid4())[:8]
        filename = f"{article['category']}_{file_id}.png"
        filepath = THUMBNAIL_DIR / filename
        
        # In a real app, we'd use PIL/Pillow here to draw text on a background.
        # For now, we save a metadata file representing the "image creation".
        
        image_meta = {
            "target_path": str(filepath),
            "overlay_text": article['title'][:40].upper(),
            "bg_color": self._get_color_for_category(article.get('category')),
            "created_at": str(filepath) # utilizing timestamp
        }
        
        # Simulate saving the asset
        # TODO: Implement actual Stable Diffusion or Pillow logic here
        with open(str(filepath) + ".meta.json", 'w') as f:
            json.dump(image_meta, f, indent=2)
            
        article['media_assets'] = {
            'thumbnail_path': str(filepath),
            'meta': image_meta
        }
        
        logger.info(f"Media assets prepared for {article['id']}")
        return article

    def _get_color_for_category(self, category: str) -> str:
        colors = {
            "politics": "#FF0000", # Red
            "finance": "#00FF00",  # Green
            "tech": "#0000FF",     # Blue
            "entertainment": "#FF00FF" # Magenta
        }
        return colors.get(category, "#000000")