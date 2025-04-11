def test_url_validity(browser):
    browser.get("https://www.guvi.in")
    assert "guvi.in" in browser.current_url
