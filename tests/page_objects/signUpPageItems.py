from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignUpPageItems:
    def __init__(self, driver):
        self.driver = driver
        self.email_input = (By.NAME, 'email')
        self.user_input = (By.NAME, 'user_name')
        self.password_input = (By.NAME, 'password')
        self.select_month_input = (By.NAME, 'birthday[month]')
        self.select_day_input = (By.NAME, 'birthday[day]')
        self.select_year_input = (By.NAME, 'birthday[year]')
        self.agreement_checkbox = (By.NAME, 'agreement')

    def enter_email(self, keys):
        enter_mail = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.email_input))
        enter_mail.send_keys(keys)
        #self.driver.find_element(*self.email_input).send_keys(keys)

    def enter_user(self, keys):
        self.driver.find_element(*self.user_input).send_keys(keys)

    def enter_password(self, keys):
        self.driver.find_element(*self.password_input).send_keys(keys)

    def select_birthday_month(self, number):
        input_birthday_element = self.driver.find_element(*self.select_month_input)
        input_birthday = Select(input_birthday_element)
        input_birthday.select_by_value(number)

    def select_birthday_day(self, number):
        input_birthday_element = self.driver.find_element(*self.select_day_input)
        input_birthday = Select(input_birthday_element)
        input_birthday.select_by_value(number)

    def select_birthday_year(self, number):
        input_birthday_element = self.driver.find_element(*self.select_year_input)
        input_birthday = Select(input_birthday_element)
        input_birthday.select_by_value(number)

    def click_agreement_checkbox(self):
        self.driver.find_element(*self.agreement_checkbox).click()