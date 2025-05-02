import pytest
from selenium import webdriver
from pages.header_page import HeaderPage
from conftest import driver
BASE_URL = "https://stellarburgers.nomoreparties.site"
FEED_URL = f"{BASE_URL}/feed"


def test_navigation_to_order_feed(driver):
    driver.get(BASE_URL)

    header = HeaderPage(driver)
    header.click_order_feed_button()

    assert driver.current_url.rstrip("/") == FEED_URL.rstrip("/"), "Переход по кнопке 'Лента заказов' не удался"
