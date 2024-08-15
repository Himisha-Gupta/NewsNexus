# NEWS NEXUS

## Overview

This project is a **multi-agent news reporting system** designed to automatically gather and report on the latest updates and advancements in various topics, with a particular focus on the impact of AI on the tech sector and jobs. The system utilizes Crew AI to orchestrate two primary agents:

- **Senior Research Agent**: Uncovers the latest updates and advancements in a given topic using custom tools and large language models (LLMs).
- **Writer Agent**: Crafts engaging narratives based on the research findings.

## Features

- **Senior Research Agent**: Identifies the next big trend in a given topic.
- **Writer Agent**: Composes insightful articles based on research findings.
- **Comprehensive Reports**: Generates detailed 3-paragraph reports on the latest trends.
- **Insightful Articles**: Produces 4-paragraph markdown-formatted articles on advancements in the topic.

## Files

- **`app.py`**: Main entry point to initialize and run the application.
- **`agents.py`**: Defines the agents used in the project (`news_researcher` and `news_writer`).
- **`tasks.py`**: Defines tasks assigned to the agents (`research_task` and `write_task`).
- **`tools.py`**: Contains custom tools used by the agents, such as `SerperDevTool`.
- **`crew.py`**: Sets up the crew (agents and tools), assigns tasks, and manages workflow.
- **`.env`**: Stores environment variables like API keys (ensure this file is  not committed)
