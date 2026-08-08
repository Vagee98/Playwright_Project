from playwright.sync_api import Page
class Logout:
    def __init__(self,page:Page):
        self.page = page
    def click_dropdown(self):
        self.page.locator(".oxd-userdropdown-icon").click()
    def logout(self):
        self.page.get_by_text("Logout").click()
