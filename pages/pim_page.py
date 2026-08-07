from playwright.sync_api import Page
class Pim_page:
    def __init__(self,page:Page):
        self.page = page
    # def click_hamburger_menu(self):
    #     self.page.screenshot(path="screenshots/before_hamburger.png")
    #     self.page.locator(".oxd-topbar-header-hamburger").click()
    def click_pim_option(self):
        self.page.get_by_text("PIM").click()
    def add_employee(self):
        self.page.get_by_role("button",name="Add").click()
    def add_employee_details(self,f_name,m_name,l_name,empid,):
        self.page.get_by_placeholder("First Name").fill(f_name)
        self.page.get_by_placeholder("Middle Name").fill(m_name)
        self.page.get_by_placeholder("Last Name").fill(l_name)
        self.page.locator("input").nth(3).fill(empid)
        # self.page.locator(".oxd-switch-input").check()
        self.page.get_by_role("button",name="save").click()
        