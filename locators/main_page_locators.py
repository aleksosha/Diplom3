from selenium.webdriver.common.by import By

class MainPageLocators:
        FIRST_INGREDIENT = (By.XPATH, '//p[text()="Флюоресцентная булка R2-D3"]/ancestor::a')
        MODAL_WINDOW = (By.XPATH, '//div[contains(@class, "Modal_modal__contentBox")]')
        MODAL_TITLE = (By.XPATH, '//h2[text()="Детали ингредиента"]')
        CLOSE_MODAL_BUTTON = (By.XPATH, '//*[@id="root"]/div/section[1]/div[1]/button')
        TARGET_AREA = (By.XPATH, '//*[text()="Перетяните булочку сюда (верх)"]')
        COUNTER = (By.CLASS_NAME, "counter_counter__ZNLkj")
        CONSTRUCTOR_ROW = (By.CLASS_NAME, "constructor-element__row")
        ORDER_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')
        ORDER_CONFIRMATION_MODAL = (By.CSS_SELECTOR, '.Modal_modal__contentBox__sCy8X')