from playwright.sync_api import Page

from config.config import UI_BASE_URL
from pom.base_page import BasePage


class PracticePage(BasePage):
    URL = f"{UI_BASE_URL}/practice/"

    def __init__(self, page: Page):
        super().__init__(page)

        self.link_login = page.locator("a[href*='practice-test-login']")
        self.link_exceptions = page.locator("a[href*='practice-test-exceptions']")
        self.link_tables = page.locator("a[href*='practice-test-table']")

    def open(self):
        self.open_url(self.URL)

    def click_login(self):
        self.click(self.link_login)

    def click_exceptions(self):
        self.click(self.link_exceptions)

    def click_tables(self):
        self.click(self.link_tables)
