import time

from playwright.sync_api import Playwright, expect


class Login:
    def __init__(self, playwright:Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()
        self.page.goto("https://www.daraz.com.np/#?")

    def login(self,data):
        self.page.get_by_role("link", name = "Login").click()
        self.page.get_by_placeholder("Please enter your Phone or Email").fill(f"{data['email']}")
        self.page.get_by_placeholder("Please enter your password").fill(data["password"])
        self.page.get_by_role("button", name = "LOGIN").click()
        time.sleep(2)
        expect(self.page.get_by_role("button", name = "LOGIN")).not_to_be_visible()

