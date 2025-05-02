import pytest
from selenium import webdriver
from pages.main_page import MainPage
from conftest import driver


BASE_URL = "https://stellarburgers.nomoreparties.site"

def test_modal_close_on_click(driver):
    driver.get(BASE_URL)

    main_page = MainPage(driver)
    main_page.click_first_ingredient()

    main_page.wait_for_modal_to_appear()

    main_page.close_modal()

    main_page.wait_for_modal_to_disappear()

