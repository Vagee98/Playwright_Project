from pages.login_page import Loginpage
from playwright.sync_api import expect
import json
import logging

logging.basicConfig(level=logging.INFO)
with open("data/login_data.json") as file:
    users = json.load(file)
def test_login(page):
    user = users[0]
    login_page = Loginpage(page)
    logging.info("We are in Login page")
    try:
        login_page.login(user["username"],user["password"])
        expect(page).to_have_url('https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index')
        logging.indo("Login Successfull")
    except Exception as e:
        print(f"Exception is {e}")
        page.screenshot(path="screenshots/login_page.png")
    

