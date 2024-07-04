import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope='function', autouse=True)
def browser_fixture():
    """
    The fixture sets up a browser with a specific viewport size, navigates
    to a webpage, and yields a Page object for test functions to interact
    with
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.set_viewport_size({'width': 1512, 'height': 880})
        page.goto("https://nativeteams.com/")
        yield page
        browser.close()
