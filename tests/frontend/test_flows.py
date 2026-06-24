from playwright.sync_api import expect

import assertions.page_assertions as page_assertions
from config.config import USERNAME, PASSWORD


def test_login_flow(
        practice_page,
        login_page,
        logged_in_page
):
    practice_page.open()
    page_assertions.expect_practice_page_loaded(practice_page)

    practice_page.click_login()
    page_assertions.expect_login_page_loaded(login_page)

    login_page.login(USERNAME, PASSWORD)
    page_assertions.expect_logged_in_page_loaded(logged_in_page)


def test_login_negative_username(
        practice_page,
        login_page,
        logged_in_page
):
    practice_page.open()
    page_assertions.expect_practice_page_loaded(practice_page)

    practice_page.click_login()
    page_assertions.expect_login_page_loaded(login_page)

    login_page.login(USERNAME + "_incorrect", PASSWORD)
    expect(login_page.error_invalid_username).to_be_visible()
    expect(login_page.error_invalid_password).not_to_be_visible()


def test_login_negative_password(
        practice_page,
        login_page,
        logged_in_page
):
    practice_page.open()
    page_assertions.expect_practice_page_loaded(practice_page)

    practice_page.click_login()
    page_assertions.expect_login_page_loaded(login_page)

    login_page.login(USERNAME, PASSWORD + "_incorrect")
    expect(login_page.error_invalid_password).to_be_visible()
    expect(login_page.error_invalid_username).not_to_be_visible()
