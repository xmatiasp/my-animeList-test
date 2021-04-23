import unittest
from selenium import webdriver
from tests.page_objects.homePageItem import HomePageItems
from tests.page_objects.signUpPageItems import SignUpPageItems
import time

class SignInCases(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('tests/drivers/chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get('https://myanimelist.net/')
        self.itemsHomePage = HomePageItems(self.driver)
        self.itemsSignUpPage = SignUpPageItems(self.driver)

    def test_sign_in_valid_mail(self):
        self.itemsHomePage.click_sign_up()
        self.itemsSignUpPage.enter_email('prueba123@gmail.com')
        self.itemsSignUpPage.enter_user('usuarioPrueba')
        self.itemsSignUpPage.enter_password('Prueba@123456')
        self.itemsSignUpPage.select_birthday_month('5')
        self.itemsSignUpPage.select_birthday_day('9')
        self.itemsSignUpPage.select_birthday_year('1992')
        self.itemsSignUpPage.click_agreement_checkbox()
        time.sleep(5)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()