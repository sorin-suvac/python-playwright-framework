from assertions.page_assertions import expect_login_page_loaded, expect_practice_page_loaded, \
    expect_logged_in_page_loaded
from config.config import USERNAME, PASSWORD


def test_practice_page(practice_page):
    practice_page.open()

    expect_practice_page_loaded(practice_page)


def test_login_page(login_page):
    login_page.open()

    expect_login_page_loaded(login_page)


def test_login_flow(
        practice_page,
        login_page,
        logged_in_page
):
    practice_page.open()
    expect_practice_page_loaded(practice_page)

    practice_page.click_login()
    expect_login_page_loaded(login_page)

    login_page.login(USERNAME, PASSWORD)
    expect_logged_in_page_loaded(logged_in_page)
