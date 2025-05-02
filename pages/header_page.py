from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.header_locators import HeaderLocators

class HeaderPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_constructor_button(self):
        constructor_button = self.wait.until(
            EC.element_to_be_clickable(HeaderLocators.CONSTRUCTOR_BUTTON)
        )
        constructor_button.click()

    def click_order_feed_button(self):
        order_feed_button = self.wait.until(
            EC.element_to_be_clickable(HeaderLocators.ORDER_FEED_BUTTON)
        )
        order_feed_button.click()
