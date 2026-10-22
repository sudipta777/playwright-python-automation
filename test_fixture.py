from playwright.sync_api import expect

def test_username(login_page):
    login_page.locator("#user-name").fill("standard_user")
    expect(login_page.locator("#user-name")).to_have_value("standard_user")