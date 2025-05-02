import pytest
from pages.main_page import MainPage
from conftest import driver

BASE_URL = "https://stellarburgers.nomoreparties.site"

def test_add_ingredient_in_basket(driver):
    driver.get(BASE_URL)

    main_page = MainPage(driver)

    main_page.drag_and_drop_ingredient()

    main_page.wait_for_ingredient_in_basket()

    counter_value = main_page.get_counter_value()

    assert counter_value == 2, f"Ожидалось число 2, но пришло {counter_value}"
