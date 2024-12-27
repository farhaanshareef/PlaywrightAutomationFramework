# tests/test_form_submission.py

import pytest
from pageObject.form_page import FormPage
from config.config import Config
from utils.logger import Logger

logger = Logger.get_logger(__name__)

@pytest.mark.parametrize("data", [
    {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@yopmail.com",
        "gender": "Male",
        "mobile": "1234567890"    }
])
def test_form_submission(page, data):
    logger.info("Starting test: test_form_submission")
    form_page = FormPage(page)
    form_page.navigate_to(Config.APP_URL)
    form_page.fill_form(data)
    logger.info("Test case completed: test_form_submission")
