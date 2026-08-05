from pages.login_page import Loginpage
from playwright.sync_api import expect
import json

with open("data/login_data.json") as file:
    users = json.load(file)
def test_login(page):
    user = users[0]
    login_page = Loginpage(page)
    login_page.login(user["username"],user["password"])
    # try:
    # expect(page.get_by_text("Dashboard")).to_be_visible()
    expect(page).to_have_url('https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index')
    # except Exception as e:
    #     print(e)

