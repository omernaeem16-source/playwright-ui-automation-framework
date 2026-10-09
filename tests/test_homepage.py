from playwright.sync_api import expect


def test_homepage(page):
    # Open the catalog page
    page.goto("https://qademo.com/catalog")

    # Verify that the catalog page loads at the expected URL
    expect(page).to_have_url("https://qademo.com/catalog")

