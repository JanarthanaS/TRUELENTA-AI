Truelenta AI – Automated News Curation System

Truelenta AI is a multi-agent Python system designed to fetch, classify, verify, rewrite, and publish news content automatically. It is designed to work with trusted Indian news sources and supports multilingual detection.

Architecture

The system relies on a pipeline of agents:

SourceCollector: RSS/HTML ingestion.

Classifier: Taxonomy and Language detection (supports Hi, En, Ta, Te).

FactCheck: 3-layer verification scoring.

Rewriter: Generates editorial summaries and social media captions.

Media: Metadata generation for assets.

Publisher: JSON output for web frontends.

Project Structure

Truelenta-AI/
├── src/
│   ├── agents/    # Business logic
│   ├── utils/     # Helpers
│   ├── config.py  # Settings
│   └── pipeline.py
├── assets/        # Generated output
└── tests/


Setup

Clone the repository

Install dependencies:

pip install -r requirements.txt


Run the pipeline:

python -m src.app


Development

Follow Google Python Style Guide.

Run tests via python -m unittest discover tests.

License

MIT License