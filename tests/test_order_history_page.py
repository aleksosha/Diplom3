import pytest
from pages.login_page import LoginPage
from conftest import driver

def test_order_history_page(driver):
    login_page = LoginPage(driver)
    login_page.open()

    login_page.enter_email("drobotunalexandra@yandex.ru")
    login_page.enter_password("drobotun123")
    login_page.click_login_button()

    account_page = login_page.click_account_button()

    assert account_page.is_account_page_opened(), "Переход на страницу Личного кабинета не выполнен"

    account_page.click_order_history_link()

    assert account_page.is_order_history_page_opened(), "Переход на страницу Истории заказов не выполнен"
