import pytest
from selenium import webdriver
from pages.header_page import HeaderPage
from conftest import driver

BASE_URL = "https://stellarburgers.nomoreparties.site"


def test_navigation_to_constructor(driver):
    driver.get(f"{BASE_URL}/feed")

    header = HeaderPage(driver)
    header.click_constructor_button()

    assert driver.current_url.rstrip('/') == BASE_URL.rstrip('/'), "Переход по кнопке 'Конструктор' не удался"

