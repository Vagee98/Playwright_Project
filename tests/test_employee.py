import pytest
from playwright.sync_api import expect
from pages.login_page import Loginpage
from pages.pim_page import Pim_page
import json
import logging

logging.basicConfig(level=logging.INFO)

with open("data/employee_data.json") as emp:
    employees = json.load(emp)
with open("data/login_data.json") as file:
    users = json.load(file)
def test_add_emplyee_details(page):
    user = users[0]
    employee = employees[0]
    login_page = Loginpage(page)
    add_details = Pim_page(page)
    logging.info("Loging to teh site")
    login_page.login(user["username"],user["password"])
    # add_details.click_hamburger_menu()
    logging.info("Adding the user details to PIM")
    try:
        add_details.click_pim_option()
        add_details.add_employee()
        add_details.add_employee_details(employee["first_name"],employee["middle_name"],employee["last_name"],employee["employee_id"])
        expect(page.locator(".oxd-toast-content")).to_be_visible()
        page.screenshot(path = "screenshots/add_emploee_success.png",full_page=True)
        logging.info("Employee details added")
    except Exception as e:
        page.screenshot("screenshots/add_emploee_failed.png",full_page=True)
        print("Exception is",e)
        logging.error("Adding employee details failed")
        raise

