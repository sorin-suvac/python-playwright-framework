from playwright.sync_api import Page

from config.config import BASE_URL
from pom.base_page import BasePage


class LoginPage(BasePage):
    URL = f"{BASE_URL}/practice-test-login/"

    def __init__(self, page: Page):
        super().__init__(page)

        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.submit_button = page.locator("#submit")

    def open(self):
        self.open_url(self.URL)

    def login(self, username: str, password: str):
        self.fill(self.username_input, username)
        self.fill(self.password_input, password)
        self.click(self.submit_button)
