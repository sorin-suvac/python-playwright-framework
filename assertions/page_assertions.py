from playwright.sync_api import expect


def expect_practice_page_loaded(practice_page):
    expect(practice_page.link_login).to_be_visible()
    expect(practice_page.link_tables).to_be_visible()
    expect(practice_page.link_exceptions).to_be_visible()


def expect_login_page_loaded(login_page):
    expect(login_page.input_username).to_be_visible()
    expect(login_page.input_password).to_be_visible()
    expect(login_page.btn_submit).to_be_visible()


def expect_logged_in_page_loaded(logged_in_page):
    expect(logged_in_page.btn_logout).to_be_visible()
