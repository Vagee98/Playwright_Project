from pages.search_employee_page import Search_employee
from playwright.sync_api import expect
from pages.login_page import Loginpage
import json
import logging

logging.basicConfig(level=logging.INFO)
with open("data/login_data.json")as file:
    users = json.load(file)
with open("data/search_employee.json")as emp:
    employees = json.load(emp)
def test_search_employee(page):
    logging.info("Loggin in to the site")
    login_page = Loginpage(page)
    user = users[0]
    employee = employees[0]
    search_employee_details = Search_employee(page)
    login_page.login(user["username"],user["password"])
    try:
        logging.info("Searching the employee")
        search_employee_details.click_PIM()
        search_employee_details.click_dropdown_button()
        search_employee_details.fill_employee_name(employee["name"])
        search_employee_details.search_button()
        logging.info("Search complted and is successfull")
        expect(page.get_by_text("No Records Found")).not_to_be_visible()
        page.screenshot(path = "screenshots/search_employee_success.png",full_page=True)
    except Exception as e:
        logging.error(e)
        expect(page.get_by_text("info")).to_be_visible()
        page.screenshot(path = "screenshots/search_employee_fail.png",full_page=True)
        raise
