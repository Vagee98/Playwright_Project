from playwright.sync_api import Page
class Loginpage:
    def __init__(self,page:Page):
        self.page = page
    def login(self,username,password):
        self.page.get_by_placeholder("Username").fill(username)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.get_by_role("button", name="Login").click()