# Playwright Web Automation Framework

## Overview
This repository contains a web automation framework built using Playwright. 
It is designed for efficient end-to-end testing of web applications, providing capabilities like cross-browser testing, parallel execution, and detailed reporting.

## Features
Cross-Browser Support: Automate across Chromium, Firefox, and WebKit browsers.
Parallel Execution: Run tests concurrently for faster feedback.
Detailed Reporting: Generate HTML reports with screenshots for failures.
Reusable Components: Modular structure for test cases, page objects, and utilities.

## Prerequisites
Python (version >= 3.8)
Playwright Python package

## Installation
### Clone the repository:
git clone https://github.com/farhaanshareef/PlaywrightAutomationFramework/

### Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

### Install dependencies:
pip install -r requirements.txt

### Install Playwright and its supported browsers:
playwright install

## Usage
### Running Tests
Run all tests:
pytest

R### un tests with a specific marker:
pytest -m smoke

### Generating Reports
Run tests and generate an HTML report:
pytest --html=reports/report.html --self-contained-html




