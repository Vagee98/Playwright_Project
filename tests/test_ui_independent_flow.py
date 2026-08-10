import pytest
from pages.login_page import Loginpage
from playwright.sync_api import expect
from pages.pim_page import Pim_page
from pages.search_employee_page import Search_employee
from pages.logout_page import Logout
import json
import logging

logging.basicConfig(filename="logs/execution.log",level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s")
logging.info("FRAMEWORK STARTED")
with open("data/login_data.json") as file:
    users = json.load(file)
with open("data/employee_data.json") as employ:
    employees = json.load(employ)
with open("data/search_employee.json")as emp:
    employees_list = json.load(emp)
@pytest.mark.parametrize("user",users)

#Test Login
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
#Test Add_Employee
def test_add_emplyee_details(logged_in_page):
    # user = users[0]
    employee = employees[0]
    # login_page = Loginpage(logged_in_page)
    add_details = Pim_page(logged_in_page)
    logging.info("Loging to teh site")
    # login_page.login(user["username"],user["password"])
    # add_details.click_hamburger_menu()
    # logging.info("Adding the user details to PIM")
    try:
        add_details.click_pim_option()
        add_details.add_employee()
        add_details.add_employee_details(employee["first_name"],employee["middle_name"],employee["last_name"],employee["employee_id"])
        expect(logged_in_page.locator(".oxd-toast-content")).to_be_visible()
        logged_in_page.screenshot(path = "screenshots/add_emploee_success.png",full_page=True)
        # logging.info("Employee details added")
    except Exception as e:
        logged_in_page.screenshot("screenshots/add_emploee_failed.png",full_page=True)
        print("Exception is",e)
        logging.error("Adding employee details failed")
        raise
#Test search_Employee
def test_search_employee(logged_in_page):
    # logging.info("Loggin in to the site")
    # login_page = Loginpage(logged_in_page)
    # user = users[0]
    employee = employees_list[0]
    search_employee_details = Search_employee(logged_in_page)
    # login_page.login(user["username"],user["password"])
    try:
        logging.info("Searching the employee")
        search_employee_details.click_PIM()
        search_employee_details.click_dropdown_button()
        search_employee_details.fill_employee_name(employee["name"])
        search_employee_details.search_button()
        logging.info("Search complted and is successfull")
        expect(logged_in_page.get_by_text("No Records Found")).not_to_be_visible()
        logged_in_page.screenshot(path = "screenshots/search_employee_success.png",full_page=True)
    except Exception as e:
        logging.error(e)
        expect(logged_in_page.get_by_text("info")).to_be_visible()
        logged_in_page.screenshot(path = "screenshots/search_employee_fail.png",full_page=True)
        raise
#Test Logout
def test_logout(logged_in_page):
    # login_page = Loginpage(logged_in_page)
    # user = users[0]
    logout_page = Logout(logged_in_page)

    # login_page.login(user["username"],user["password"])
    try:
        logout_page.click_dropdown()
        logout_page.logout()
        expect(logged_in_page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        logged_in_page.wait_for_timeout(3000)
        logged_in_page.screenshot(path="screenshots/logout_success.png",full_page=True)
    except Exception as e:    
        logging.error(e)
        logged_in_page.screenshot(path="screenshots/logout_fail.png",full_page=True)
        raise

    

