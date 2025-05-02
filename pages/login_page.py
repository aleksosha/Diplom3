from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.account_page_locators import AccountPageLocators
from locators.login_page_locators import LoginPageLocators
from pages.account_page import AccountPage


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/login")

    def enter_email(self, email):
        email_field = self.driver.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

    def click_account_button(self):
        account_button = self.driver.find_element(*AccountPageLocators.ACCOUNT_BUTTON)
        account_button.click()
        self.wait.until(expected_conditions.url_to_be(AccountPageLocators.ACCOUNT_PAGE_URL))
        return AccountPage(self.driver)
