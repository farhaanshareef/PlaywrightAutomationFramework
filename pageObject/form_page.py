# pages/form_page.py
from pageObject.base_page import BasePage

class FormPage(BasePage):
    def fill_form(self, data: dict):
        self.logger.info("Filling the form with provided data")

        self.fill_input("#firstName", data["first_name"])
        self.fill_input("#lastName", data["last_name"])
        self.fill_input("#userEmail", data["email"])
        self.click_element(f"//label[contains(text(), '{data['gender']}')]")
        self.fill_input("#userNumber", data["mobile"])

        self.logger.info("Filling date of birth")
        self.click_element("#dateOfBirthInput")
        self.fill_input("#dateOfBirthInput", "01 01 1996")

        self.logger.info("Submitting the form")
        self.click_element("#submit")

