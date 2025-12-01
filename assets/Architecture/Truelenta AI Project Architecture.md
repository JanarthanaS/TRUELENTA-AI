Truelenta AI: Autonomous Multi-Agent News Curation Pipeline Architecture

This document outlines the high-level architecture of the Truelenta AI system, which is based on a linear, specialized Multi-Agent pattern. Data flows sequentially through the agents, with each step adding value, verification, or transformation.

System Overview (Data Flow)

The system is designed as a secure pipeline where content is progressively filtered, verified, and enhanced. Only content that meets the VALIDATION_THRESHOLD proceeds past the FactCheckAgent.

graph TD
    A[Trusted RSS Feeds] --> B(SourceCollectorAgent);
    B --> C(ClassifierAgent);
    C --> D(FactCheckAgent);
    D -- Score >= 0.6 --> E(RewriteAgent);
    D -- Score < 0.6 --> F(MonitoringAgent / Discard);
    E --> G(PublisherAgent);
    G --> H[Final Structured JSON Output];
    B, C, D, E, G --> I(MonitoringAgent);


Agent Responsibilities and Data Transformations

1. SourceCollectorAgent (Ingestion Layer)

Function

Description

Input

List of RSS Feed URLs (config.py)

Process

Fetches, parses, and cleans raw articles (title, summary, link). Filters duplicates.

Output

Raw Article Dictionary {title, summary, link, raw_content}

2. ClassifierAgent (Editorial Layer)

Function

Description

Input

Raw Article Dictionary

Process

Uses heuristic NLP to detect the primary language and categorize the content (e.g., Politics, Finance, Tech).

Output

Classified Article Dictionary {..., category, language}

3. FactCheckAgent (Integrity Layer - The Gate)

Function

Description

Input

Classified Article Dictionary

Process

Executes the 3-tier verification: Source Credibility, Information Density, and Semantic Consistency Check. Calculates a composite verification_score.

Output

Verified Article Dictionary {..., verification_score, is_verified}. Blocks articles below the threshold.

4. RewriteAgent (Content Generation Layer)

Function

Description

Input

Verified Article Dictionary (is_verified = True)

Process

Rewrites the summary into a clean, editorial text. Generates platform-specific content (Instagram captions, YouTube Shorts scripts, hashtags).

Output

Enhanced Article Dictionary {..., editorial_text, social_content}

5. PublisherAgent (Distribution Layer)

Function

Description

Input

Enhanced Article Dictionary

Process

Finalizes metadata, sets the publish date, and serializes the complete article into a structured JSON file.

Output

Final JSON File written to assets/sample_output/

6. MonitoringAgent (Observability)

Function

Description

Process

Logs all agent activities, errors, and throughput metrics, providing real-time system visibility and statistics upon pipeline completion.

Key Architectural Principles

Modularity: Each agent is a standalone class responsible for a single function, ensuring easy maintenance and replacement.

Separation of Concerns: Verification (FactCheck) is strictly separated from Content Generation (Rewrite).

Pipeline Orchestration: The app.py script acts as the orchestrator, controlling the flow and error handling between agents.

Configuration Driven: Key thresholds and sources are defined in config.py, allowing the system rules to be adjusted without modifying agent logic.