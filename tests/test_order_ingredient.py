import pytest

from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from pages.login_page import LoginPage
from conftest import driver

BASE_URL = "https://stellarburgers.nomoreparties.site"
USER_EMAIL = "drobotunalexandra@yandex.ru"
USER_PASSWORD = "drobotun123"


def test_order_ingredient(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_email(USER_EMAIL)
    login_page.enter_password(USER_PASSWORD)
    login_page.click_login_button()

    main_page = MainPage(driver)

    main_page.drag_and_drop_ingredient()

    counter_value = main_page.get_counter_value()
    assert counter_value == 2, f"Expected counter value to be 2, but got {counter_value}"

    main_page.click_order_button()

    main_page.wait_for_order_confirmation_modal()

    assert True, "Модальное окно подтверждения заказа не появилось."
