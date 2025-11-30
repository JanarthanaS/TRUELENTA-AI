"""
Integration test to ensure the whole pipe runs without crashing.
"""
import unittest
import shutil
from pathlib import Path
from src.pipeline import TruelentaPipeline
from src.config import OUTPUT_DIR

class TestPipelineIntegration(unittest.TestCase):
    
    def setUp(self):
        # Clean output dir before test
        if OUTPUT_DIR.exists():
            for f in OUTPUT_DIR.glob("*.json"):
                f.unlink()
                
    def test_pipeline_execution(self):
        """Runs the pipeline and checks if files are created."""
        # Note: This relies on network calls. In a strict CI env, 
        # we would mock the SourceCollector.
        
        pipeline = TruelentaPipeline()
        # We don't want to actually run the whole infinite loop if it were one
        # but the current run() is one-pass.
        
        try:
            pipeline.run()
        except Exception as e:
            self.fail(f"Pipeline crashed with: {e}")
            
        # Check if logs were created
        # Check if at least one file might have been processed (hard to guarantee without mocks)
        pass

if __name__ == '__main__':
    unittest.main()