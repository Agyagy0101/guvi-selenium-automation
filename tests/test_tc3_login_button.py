from pages.home_page import HomePage

def test_login_button(browser):
    page = HomePage(browser)
    page.visit("https://www.guvi.in")
    assert page.login_button_visible()
    assert page.login_button_clickable()
