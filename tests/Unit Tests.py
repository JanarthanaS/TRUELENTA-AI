"""
Unit tests for individual agents.
"""
import unittest
from src.utils.language_utils import detect_language
from src.agents.classifier_agent import ClassifierAgent
from src.agents.fact_check_agent import FactCheckAgent

class TestAgents(unittest.TestCase):
    
    def test_language_detection(self):
        self.assertEqual(detect_language("Hello World"), "en")
        self.assertEqual(detect_language("नमस्ते भारत"), "hi")
        
    def test_classifier_logic(self):
        agent = ClassifierAgent()
        mock_article = {
            "title": "New Election Results Announced",
            "summary": "The prime minister voted today."
        }
        result = agent.process(mock_article)
        self.assertEqual(result['category'], 'politics')
        
    def test_fact_checker_score(self):
        agent = FactCheckAgent()
        mock_article = {
            "id": "1",
            "link": "https://www.ndtv.com/india-news/story",
            "summary": "This is a long enough summary to pass the keyword density check logic inside the agent.",
            "title": "Test Title"
        }
        result = agent.verify(mock_article)
        self.assertTrue(result['verification_score'] > 0.5)

if __name__ == '__main__':
    unittest.main()