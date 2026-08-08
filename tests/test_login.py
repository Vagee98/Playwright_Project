import pytest
from pages.login_page import Loginpage
from playwright.sync_api import expect
import json
import logging

logging.basicConfig(filename="logs/execution.log",level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s")
logging.info("FRAMEWORK STARTED")
with open("data/login_data.json") as file:
    users = json.load(file)
@pytest.mark.parametrize("user",users)
def test_login(page,user):
    login_page = Loginpage(page)
    logging.info("We are in Login page")
    try:
        logging.info("Attempting Login")
        login_page.login(user["username"],user["password"])
        expect(page).to_have_url('https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index')
        page.wait_for_timeout(3000)
        page.screenshot(path="screenshots/login_success.png",full_page = True)
        logging.info("Login Successfull")
    except Exception as e:
        print(f"Exception is {e}")
        page.screenshot(path="screenshots/login_failed.png",full_page = True)
        logging.info("Login Failed")
        raise
        
    

