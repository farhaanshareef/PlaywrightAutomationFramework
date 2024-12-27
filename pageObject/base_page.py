from playwright.sync_api import Page
from utils.logger import Logger

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = Logger.get_logger(self.__class__.__name__)

    def navigate_to(self, url: str):
        self.logger.info(f"Navigating to URL: {url}")
        self.page.goto(url)

    def fill_input(self, locator: str, value: str):
        self.logger.info(f"Filling input {locator} with value: {value}")
        self.page.fill(locator, value)

    def click_element(self, locator: str):
        self.logger.info(f"Clicking element: {locator}")
        self.page.click(locator)

    def select_dropdown(self, locator: str, value: str):
        self.logger.info(f"Selecting dropdown {locator} with value: {value}")
        self.page.select_option(locator, value)

