# tests/conftest.py

import pytest
from playwright.sync_api import sync_playwright
from utils.logger import Logger

logger = Logger.get_logger(__name__)

@pytest.fixture(scope="function")
def page():
    logger.info("Starting Playwright browser")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            viewport=None  # This maximizes the window
        )
        page = context.new_page()
        yield page
        logger.info("Closing Playwright browser")
        browser.close()
