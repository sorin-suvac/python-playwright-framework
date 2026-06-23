import pytest

from pom.pages.logged_in_page import LoggedInPage
from pom.pages.login_page import LoginPage
from pom.pages.practice_page import PracticePage


@pytest.fixture
def practice_page(page):
    return PracticePage(page)


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def logged_in_page(page):
    return LoggedInPage(page)
