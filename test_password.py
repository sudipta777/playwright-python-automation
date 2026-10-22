from playwright.sync_api import expect

def test_password(login_page):
    login_page.locator("#password").fill("secret_sauce")
    expect(login_page.locator("#password")).to_have_value("secret_sauce")