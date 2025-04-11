from pages.home_page import HomePage

def test_signup_button(browser):
    page = HomePage(browser)
    page.visit("https://www.guvi.in")
    assert page.signup_button_visible()
    assert page.signup_button_clickable()
