from pages.login_page import LoginPage

def test_valid_login(browser):
    page = LoginPage(browser)
    page.visit("https://www.guvi.in/sign-in/")
    page.login("valid_email@example.com", "valid_password")
    assert page.is_displayed(*page.PROFILE_ICON)
