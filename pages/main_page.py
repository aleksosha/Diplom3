from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.locators = MainPageLocators  # используем локаторы напрямую

    def click_first_ingredient(self):
        ingredient = self.wait.until(
            EC.element_to_be_clickable(self.locators.FIRST_INGREDIENT)
        )
        ingredient.click()

    def wait_for_modal_to_appear(self):
        self.wait.until(
            EC.visibility_of_element_located(self.locators.MODAL_WINDOW)
        )

    def close_modal(self):
        self.wait_for_modal_to_appear()  # Убедитесь, что модалка открылась
        close_btn = self.wait.until(
            EC.element_to_be_clickable(self.locators.CLOSE_MODAL_BUTTON)
        )
        close_btn.click()

    def wait_for_modal_to_disappear(self):
        self.wait.until(
            EC.invisibility_of_element_located(self.locators.MODAL_WINDOW)
        )

    def drag_and_drop_ingredient(self):
        # Находим ингредиент
        ingredient = self.driver.find_element(*MainPageLocators.FIRST_INGREDIENT)
        # Находим область для перетаскивания
        target_area = self.driver.find_element(*MainPageLocators.TARGET_AREA)

        # Выполняем перетаскивание
        actions = ActionChains(self.driver)
        actions.click_and_hold(ingredient).move_to_element(target_area).release().perform()

    def wait_for_ingredient_in_basket(self):
        # Ждем, пока ингредиент появится в корзине
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.CONSTRUCTOR_ROW)
        )

    def get_counter_value(self):
        # Получаем значение счетчика
        counter = self.driver.find_element(*MainPageLocators.COUNTER)
        return int(counter.text.strip())

    def click_order_button(self):
        order_button = self.driver.find_element(*MainPageLocators.ORDER_BUTTON)
        order_button.click()

    def wait_for_order_confirmation_modal(self):
        # Ожидаем, пока появится модальное окно подтверждения заказа
        self.wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_CONFIRMATION_MODAL))