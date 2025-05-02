from pages.feed_page import FeedPage
from conftest import driver

def test_order_modal_opens(driver):
    page = FeedPage(driver)
    page.open()
    page.click_first_order()
    assert page.is_modal_opened(), "Модальное окно не открылось"
