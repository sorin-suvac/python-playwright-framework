from playwright.sync_api import Page

from config.config import BASE_URL
from pom.base_page import BasePage


class LoggedInPage(BasePage):
    URL = f"{BASE_URL}/logged-in-successfully/"

    def __init__(self, page: Page):
        super().__init__(page)

        self.btn_logout = page.locator("text=Log out")

    def open(self):
        self.open_url(self.URL)

    def logout(self):
        self.btn_logout.click()
