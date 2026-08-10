import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import Loginpage
import json

with open("data/login_data.json")as file:
    users = json.load(file)
@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        yield page
        browser.close()
@pytest.fixture
def logged_in_page(page):
    user = users[0]
    login_page = Loginpage(page)
    login_page.login(user["username"],user["password"])
    yield page