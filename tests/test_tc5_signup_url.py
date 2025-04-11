def test_signup_url(browser):
    browser.get("https://www.guvi.in/sign-in/")
    assert "sign-in" in browser.current_url
