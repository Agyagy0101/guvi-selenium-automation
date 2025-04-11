class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def visit(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def find(self, by, value):
        return self.driver.find_element(by, value)

    def is_displayed(self, by, value):
        try:
            return self.find(by, value).is_displayed()
        except Exception:
            return False

    def is_clickable(self, by, value):
        try:
            element = self.find(by, value)
            return element.is_enabled()
        except Exception:
            return False
