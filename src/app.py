"""
Entry point for the Truelenta AI system.
"""
import sys
import argparse
from src.pipeline import TruelentaPipeline

def main():
    parser = argparse.ArgumentParser(description="Truelenta AI News Curator")
    parser.add_argument('--once', action='store_true', help='Run once and exit')
    parser.add_argument('--daemon', action='store_true', help='Run in loop (Not implemented yet)')
    
    args = parser.parse_args()
    
    # Initialize Pipeline
    pipeline = TruelentaPipeline()
    
    if args.daemon:
        print("Daemon mode coming soon. Running once.")
        
    pipeline.run()

if __name__ == "__main__":
    main()