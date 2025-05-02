import pytest
from pages.forgot_password_page import ForgotPasswordPage
from conftest import driver

def test_password_visibility_on_eye_icon_click(driver):
    forgot_password_page = ForgotPasswordPage(driver)
    forgot_password_page.open()
    forgot_password_page = ForgotPasswordPage(driver)
    forgot_password_page.open()
    forgot_password_page.click_forgot_password_link()
    forgot_password_page.reset_password("testemail@example.com")
    forgot_password_page.click_eye_icon()

    assert forgot_password_page.is_password_field_visible(), "Пароль не стал видимым"
