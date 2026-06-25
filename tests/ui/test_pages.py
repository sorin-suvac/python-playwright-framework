import pytest

import assertions.page_assertions as page_assertions


@pytest.mark.ui
def test_practice_page(practice_page):
    practice_page.open()

    page_assertions.expect_practice_page_loaded(practice_page)


@pytest.mark.ui
def test_login_page(login_page):
    login_page.open()

    page_assertions.expect_login_page_loaded(login_page)
