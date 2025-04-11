from pages.login_page import LoginPage

def test_valid_login(browser):
    page = LoginPage(browser)
    page.visit("https://www.guvi.in/sign-in/")
    page.login("agustineagy23417@gmail.com", "Sandy@01")
    assert page.is_displayed(*page.PROFILE_ICON)
