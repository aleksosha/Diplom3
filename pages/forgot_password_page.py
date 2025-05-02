from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.forgot_password_page_locators import ForgotPasswordPageLocators


class ForgotPasswordPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/login")

    def click_forgot_password_link(self):
        forgot_password_link = self.driver.find_element(*ForgotPasswordPageLocators.FORGOT_PASSWORD_LINK)
        forgot_password_link.click()

    def reset_password(self, email):
        email_field = self.driver.find_element(*ForgotPasswordPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)

        reset_button = self.driver.find_element(*ForgotPasswordPageLocators.RESET_BUTTON)
        reset_button.click()

        self.wait.until(EC.url_contains("/reset-password"))

    def click_eye_icon(self):
        eye_icon = self.driver.find_element(*ForgotPasswordPageLocators.EYE_ICON)
        eye_icon.click()

    def is_password_field_visible(self):
        password_field = self.driver.find_element(*ForgotPasswordPageLocators.PASSWORD_FIELD)
        return password_field.get_attribute('type') == 'text'