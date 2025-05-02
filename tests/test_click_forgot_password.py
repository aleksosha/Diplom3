from pages.forgot_password_page import ForgotPasswordPage
from conftest import driver

def test_navigate_to_forgot_password_page(driver):
    forgot_password_page = ForgotPasswordPage(driver)
    forgot_password_page.open()
    forgot_password_page.click_forgot_password_link()

    assert "/forgot-password" in driver.current_url, "Переход на страницу восстановления пароля не выполнен"