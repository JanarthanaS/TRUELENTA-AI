"""
The main orchestrator that connects all agents into a workflow.
"""
from src.agents.source_collector import SourceCollectorAgent
from src.agents.classifier_agent import ClassifierAgent
from src.agents.fact_check_agent import FactCheckAgent
from src.agents.rewrite_agent import RewriteAgent
from src.agents.media_agent import MediaAgent
from src.agents.publisher_agent import PublisherAgent
from src.agents.monitoring_agent import MonitoringAgent
from src.utils.logger import get_logger

logger = get_logger("Pipeline")

class TruelentaPipeline:
    
    def __init__(self):
        # Initialize all agents
        self.collector = SourceCollectorAgent()
        self.classifier = ClassifierAgent()
        self.fact_checker = FactCheckAgent()
        self.rewriter = RewriteAgent()
        self.media_gen = MediaAgent()
        self.publisher = PublisherAgent()
        self.monitor = MonitoringAgent()

    def run(self):
        """Executes the end-to-end pipeline."""
        logger.info("Starting Truelenta Pipeline...")
        
        try:
            # Step 1: Ingest
            articles = self.collector.collect_news()
            
            for article in articles:
                self.monitor.articles_processed += 1
                
                # Step 2: Classify
                article = self.classifier.process(article)
                
                # Step 3: Verify
                article = self.fact_checker.verify(article)
                
                # Gate: If verification score is too low, maybe we drop it?
                # For now, we let it pass but marked as unverified.
                
                # Step 4: Rewrite
                article = self.rewriter.process(article)
                
                # Step 5: Media
                article = self.media_gen.generate_assets(article)
                
                # Step 6: Publish
                success = self.publisher.publish(article)
                
                if not success:
                    logger.warning(f"Failed to publish {article['id']}")

        except KeyboardInterrupt:
            logger.info("Pipeline stopped by user.")
        except Exception as e:
            self.monitor.errors += 1
            logger.exception("Critical pipeline error")
        finally:
            self.monitor.log_stats()

if __name__ == "__main__":
    TruelentaPipeline().run()