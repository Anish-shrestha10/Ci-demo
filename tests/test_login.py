from playwright.sync_api import Playwright

from pages.login import Login


def test_login(playwright:Playwright):
    obj = Login(playwright)
    obj.login(
        {
            "email":"anish.shrestha7077@gmail.com",
            "password":"okchata@123",
        })