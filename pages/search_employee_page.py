from playwright.sync_api import Page
import pytest
class Search_employee:
    def __init__(self,page:Page):
        self.page = page
    def click_PIM(self):
        self.page.get_by_text("PIM").click()
    def click_dropdown_button(self):
        self.page.locator("button.oxd-icon-button").first.click()
    def fill_employee_name(self,empname):
        self.page.get_by_role("textbox").nth(1).fill(empname)
    def fill_employee_id(self,empid):
        self.page.get_by_label("Employee Id").fill(empid)
    def search_button(self):
        self.page.get_by_role("button",name="Search").click()