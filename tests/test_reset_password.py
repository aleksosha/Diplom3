import pytest
from pages.forgot_password_page import ForgotPasswordPage
from conftest import driver
def test_navigate_to_reset_password_page(driver):
    forgot_password_page = ForgotPasswordPage(driver)
    forgot_password_page.open()
    forgot_password_page.click_forgot_password_link()
    forgot_password_page.reset_password("testemail@example.com")

    assert "/reset-password" in driver.current_url, "Переход на страницу сброса пароля не выполнен"