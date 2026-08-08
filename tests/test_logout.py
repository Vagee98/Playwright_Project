from playwright.sync_api import expect
from pages.logout_page import Logout
from pages.login_page import Loginpage
import json
import logging
logging.basicConfig(level=logging.INFO)

with open("data/login_data.json")as file:
    users = json.load(file)
def test_logout(page):
    login_page = Loginpage(page)
    user = users[0]
    logout_page = Logout(page)

    login_page.login(user["username"],user["password"])
    try:
        logout_page.click_dropdown()
        logout_page.logout()
        expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        page.wait_for_timeout(3000)
        page.screenshot(path="screenshots/logout_success.png",full_page=True)
    except Exception as e:    
        logging.error(e)
        page.screenshot(path="screenshots/logout_fail.png",full_page=True)
        raise

