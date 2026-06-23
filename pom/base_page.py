from playwright.sync_api import Page


class BasePage:

    def __init__(self, page: Page):
        self.page = page
        self.page.set_default_timeout(10000)
        self.page.set_default_navigation_timeout(30000)

    def open_url(self, url: str):
        self.page.goto(url)

    @staticmethod
    def click(locator):
        locator.click()

    @staticmethod
    def fill(locator, text: str):
        locator.fill(text)

    def get_title(self):
        return self.page.title()

    def current_url(self):
        return self.page.url

    def take_screenshot(self, name: str):
        self.page.screenshot(
            path=f"screenshots/{name}.png"
        )
