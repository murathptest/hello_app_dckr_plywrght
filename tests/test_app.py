from playwright.sync_api import sync_playwright

def test_homepage_and_form_submit():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://192.168.1.33:5000")  # replace with laptop IP
        assert page.text_content("h1").strip() == "Hello World App"
        page.fill('input[name="textfield"]', 'hello-playwright')
        page.check('input[name="check"]')
        page.click('input[type="submit"]')
        body_text = page.text_content("body")
        assert "Text: hello-playwright" in body_text
        assert "Checkbox: yes" in body_text
        browser.close()

