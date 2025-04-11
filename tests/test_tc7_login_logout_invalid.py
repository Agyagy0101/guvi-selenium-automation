from pages.login_page import LoginPage

def test_invalid_login(browser):
    page = LoginPage(browser)
    page.visit("https://www.guvi.in/sign-in/")
    page.login("invalid@example.com", "wrongpass")
    assert "invalid" in page.get_error().lower()

def test_logout(browser):
    page = LoginPage(browser)
    page.visit("https://www.guvi.in/sign-in/")
    page.login("valid_email@example.com", "valid_password")
    assert page.is_displayed(*page.PROFILE_ICON)
    page.logout()
    assert not page.is_displayed(*page.PROFILE_ICON)
