import pytest
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture()
def page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()