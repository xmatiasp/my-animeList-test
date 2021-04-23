from selenium.webdriver.common.by import By

class HomePageItems:
    def __init__(self, driver):
        self.driver = driver
        self.signIn_button = (By.CLASS_NAME, 'btn-signup')

    def click_sign_up(self):
        self.driver.find_element(*self.signIn_button).click()