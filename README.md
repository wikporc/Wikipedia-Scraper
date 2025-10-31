# Wikipedia-Scraper
A simple wikipedia scraper made as a submission project for BeCode AI &amp; Data Science Bootcamp

Lightweight scraper that collects current national leaders from Wikipedia and writes them to a JSON file.

## Overview
This project fetches leader information (e.g., heads of state, heads of government) for countries from Wikipedia and stores results in `leaders_output.json`. It includes a reusable scraper module, a small CLIable `main.py`, and a test for the fetch logic.

## Features
- Scrape leader details for countries from Wikipedia
- Structured output as JSON (`leaders_output.json`)
- Testable scraper functions
- Example notebook for exploration (`wikipedia_scraper.ipynb`)

## Requirements
- Python (written using 3.13.7, should work on older versions)
- Requests
- BeautifulSoup4


## Install dependencies:
- Create venv (Windows)
  - python -m venv .venv
  - .venv\Scripts\activate
- Install
  - pip install -r requirements.txt
  - If no requirements.txt: pip install requests beautifulsoup4 pytest

## Usage
Run the scraper:
- From repository root:
  - python main.py

The script writes/updates `leaders_output.json` in the project root.

## Project layout
- main.py — entry point that runs the scraper and writes output
- leaders_output.json — sample/output file with scraped leaders
- scraper/
  - country_scraper.py — scraping logic for country pages
  - leader.py — leader data model (structures/serialisation)
  - utils.py — helper utilities for HTTP, parsing, etc.
- test_fetch.py — a simplified testing script
- wikipedia_scraper.ipynb — exploratory notebook

## Notes & Tips
- Wikipedia page structure can change; selectors in `scraper/country_scraper.py` may need updating.
- Use the notebook for debugging and inspecting intermediate HTML/parsing results.
- If scraping a large number of pages, respect robots.txt and add request delays.

