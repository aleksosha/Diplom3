from pages.feed_page import FeedPage
from conftest import driver

def test_order_list_visible_on_feed_page(driver):
    page = FeedPage(driver)
    page.open()
    assert page.is_order_list_displayed(), "Список заказов не отображается на странице /feed"
