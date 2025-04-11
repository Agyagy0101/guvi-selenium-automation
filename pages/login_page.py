from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.XPATH, "//button[text()='Login']")
    ERROR_MSG = (By.CLASS_NAME, "error")
    PROFILE_ICON = (By.XPATH, "//img[@alt='Profile']")
    LOGOUT_BTN = (By.LINK_TEXT, "Logout")

    def login(self, email, password):
        self.find(*self.EMAIL).send_keys(email)
        self.find(*self.PASSWORD).send_keys(password)
        self.find(*self.SUBMIT).click()

    def get_error(self):
        return self.find(*self.ERROR_MSG).text

    def logout(self):
        self.find(*self.PROFILE_ICON).click()
        self.find(*self.LOGOUT_BTN).click()
