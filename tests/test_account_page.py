import pytest
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from conftest import driver


def test_account_page(driver):
    login_page = LoginPage(driver)
    login_page.open()

    login_page.enter_email("drobotunalexandra@yandex.ru")
    login_page.enter_password("drobotun123")

    login_page.click_login_button()
    account_page = login_page.click_account_button()

    assert account_page.is_account_page_opened(), "Переход на страницу Личного кабинета не выполнен"


