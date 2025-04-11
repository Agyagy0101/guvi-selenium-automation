from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    LOGIN_BTN = (By.LINK_TEXT, "Login")
    SIGNUP_BTN = (By.LINK_TEXT, "Sign up")

    def login_button_visible(self):
        return self.is_displayed(*self.LOGIN_BTN)

    def login_button_clickable(self):
        return self.is_clickable(*self.LOGIN_BTN)

    def signup_button_visible(self):
        return self.is_displayed(*self.SIGNUP_BTN)

    def signup_button_clickable(self):
        return self.is_clickable(*self.SIGNUP_BTN)
