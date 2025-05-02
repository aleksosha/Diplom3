import pytest
from selenium import webdriver
from pages.main_page import MainPage
from conftest import driver

BASE_URL = "https://stellarburgers.nomoreparties.site"

def test_ingredient_modal_opens(driver):
    driver.get(BASE_URL)

    main_page = MainPage(driver)
    main_page.click_first_ingredient()

    assert main_page.is_ingredient_modal_visible(), "Модальное окно не открылось"
    assert main_page.get_modal_title_text() == "Детали ингредиента", "Заголовок модального окна некорректен"
