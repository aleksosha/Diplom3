from locators.feed_locators import FeedPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FeedPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/feed")

    def click_first_order(self):
        self.wait.until(EC.element_to_be_clickable(FeedPageLocators.FIRST_ORDER)).click()

    def is_modal_opened(self):
        return self.wait.until(EC.visibility_of_element_located(FeedPageLocators.MODAL_TITLE))

    def is_order_list_displayed(self):
        return self.wait.until(EC.visibility_of_element_located(FeedPageLocators.ORDER_LIST))