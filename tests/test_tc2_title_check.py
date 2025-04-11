def test_title(browser):
    browser.get("https://www.guvi.in")
    assert browser.title == "GUVI | Learn to code in your native language"
