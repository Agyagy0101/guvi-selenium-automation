from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class LoginPage(BasePage):
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.XPATH, "//button[text()='Login']")
    ERROR_MSG = (By.CLASS_NAME, "error")
    PROFILE_ICON = (By.XPATH, "//img[@alt='Profile']")
    LOGOUT_BTN = (By.LINK_TEXT, "Logout")

    def login(self, email, password):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.EMAIL)).send_keys(email)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.PASSWORD)).send_keys(password)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SUBMIT)).click()

    def get_error(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.ERROR_MSG)).text

    def logout(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.PROFILE_ICON)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.LOGOUT_BTN)).click()
