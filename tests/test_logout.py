import pytest
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from conftest import driver

def test_logout(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_email("drobotunalexandra@yandex.ru")
    login_page.enter_password("drobotun123")
    login_page.click_login_button()
    account_page = login_page.click_account_button()

    assert account_page.is_account_page_opened(), "Не открылась страница личного кабинета"

    account_page.click_logout_button()

    assert account_page.is_login_page_opened(), "Не произошёл переход на страницу логина после выхода"
