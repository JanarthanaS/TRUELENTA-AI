"""
Agent responsible for editorial rewriting and content generation.
Generates Social Media captions and Scripts.
"""
import random
from typing import Dict, Any
from src.utils.logger import get_logger

logger = get_logger(__name__)

class RewriteAgent:
    """Uses templates to simulate editorial intelligence."""

    def __init__(self):
        self.intros = [
            "Here is what's happening today:",
            "Breaking update:",
            "Just in:",
            "Latest report suggests:"
        ]
        
        self.outros = [
            "Stay tuned for more.",
            "Follow Truelenta for updates.",
            "What do you think? Let us know."
        ]

    def _generate_editorial_summary(self, title: str, summary: str) -> str:
        """Combines snippets into a cohesive paragraph."""
        intro = random.choice(self.intros)
        # Simple string manipulation to clean up RSS quirks
        clean_summ = summary.replace("Read more", "").strip()
        return f"{intro} {clean_summ}"

    def _generate_insta_caption(self, title: str, hashtags: list) -> str:
        """Creates an engaging caption."""
        return f"🚨 {title}\n\nSwipe to read the full story. 👉\n\n{' '.join(hashtags)}"

    def _generate_shorts_script(self, title: str, summary: str) -> str:
        """Creates a ~60s script format."""
        return (
            f"[SCENE: FAST CUTS / NEWS BG]\n"
            f"HOST: {title}\n"
            f"VO: {summary[:100]}...\n"
            f"HOST: Subscribe for more updates!"
        )

    def process(self, article: Dict[str, Any]) -> Dict[str, Any]:
        """Runs the rewriting pipeline on an article."""
        
        # Skip if low confidence
        if not article.get('is_verified', False):
            logger.warning(f"Skipping rewrite for unverified article: {article['id']}")
            return article

        cat = article.get('category', 'general')
        
        # 1. Editorial Rewrite
        article['editorial_text'] = self._generate_editorial_summary(
            article['title'], article['summary']
        )
        
        # 2. Hashtags
        tags = [f"#{cat}", "#news", "#truelenta", f"#{article['language']}News"]
        
        # 3. Social Content
        article['social_content'] = {
            'instagram_caption': self._generate_insta_caption(article['title'], tags),
            'youtube_script': self._generate_shorts_script(article['title'], article['summary']),
            'hashtags': tags
        }
        
        logger.debug(f"Generated content for {article['id']}")
        return article