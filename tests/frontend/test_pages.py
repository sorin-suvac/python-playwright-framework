import assertions.page_assertions as page_assertions


def test_practice_page(practice_page):
    practice_page.open()

    page_assertions.expect_practice_page_loaded(practice_page)


def test_login_page(login_page):
    login_page.open()

    page_assertions.expect_login_page_loaded(login_page)
