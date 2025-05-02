from selenium.webdriver.common.by import By

class FeedPageLocators:
    FIRST_ORDER = (By.XPATH, '//*[@id="root"]/div/main/div/div/ul/li[1]')
    MODAL_TITLE = (By.XPATH, '//*[@id="root"]/div/section[2]/div[1]/div')
    ORDER_LIST = (By.XPATH, '//*[@id="root"]/div/main/div/div/ul')
