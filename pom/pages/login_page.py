from playwright.sync_api import Page

from config.config import UI_BASE_URL
from pom.base_page import BasePage


class LoginPage(BasePage):
    URL = f"{UI_BASE_URL}/practice-test-login/"

    def __init__(self, page: Page):
        super().__init__(page)

        self.input_username = page.locator("#username")
        self.input_password = page.locator("#password")
        self.btn_submit = page.locator("#submit")
        self.error_invalid_username = page.locator('#error:has-text("Your username is invalid!")')
        self.error_invalid_password = page.locator('#error:has-text("Your password is invalid!")')

    def open(self):
        self.open_url(self.URL)

    def login(self, username: str, password: str):
        self.fill(self.input_username, username)
        self.fill(self.input_password, password)
        self.click(self.btn_submit)
