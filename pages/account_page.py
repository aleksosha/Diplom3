# account_page.py

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.account_page_locators import AccountPageLocators

class AccountPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_account_page_opened(self):
        """Проверяем, что открыта страница личного кабинета"""
        return self.driver.current_url == AccountPageLocators.ACCOUNT_PAGE_URL

    def click_order_history_link(self):
        """Кликаем по ссылке 'История заказов'"""
        order_history_link = self.driver.find_element(*AccountPageLocators.ORDER_HISTORY_LINK)
        order_history_link.click()
        self.wait.until(EC.url_to_be("https://stellarburgers.nomoreparties.site/account/order-history"))

    def is_order_history_page_opened(self):
        """Проверяем, что открыта страница истории заказов"""
        return self.driver.current_url == "https://stellarburgers.nomoreparties.site/account/order-history"

    def click_logout_button(self):
        """Кликаем по кнопке 'Выход'"""
        logout_button = self.driver.find_element(*AccountPageLocators.LOGOUT_BUTTON)
        logout_button.click()

        # Ожидаем, что страница логина будет загружена
        self.wait.until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))

    def is_login_page_opened(self):
        """Проверяем, что открыта страница логина"""
        return self.driver.current_url == "https://stellarburgers.nomoreparties.site/login"
