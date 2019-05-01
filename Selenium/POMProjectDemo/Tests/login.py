"""
Small Sample Project: using Page Object Model (POM)
Scope:
1. Create a simple login-logout test
    1.1 set time sleep for 2sec before close browser
2. implement unit testing
    2.1 Execute in command line: > python -m unittest login.py
    2.2 Execute in command line: > python login.py   #without -m unittest
        # Add following code with
        if __name__ == '__main__':
            unittest.main()
3. Implement Page Object Model
4. Separate test scripts and objects
5. Create a separate class for Locators
6. Run from command line : 套用POM 架構後, 在 command line 執行會出錯，所以需要加入以下ˇ:
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
7. Add HTML Reports
//*[@id="spanMessage"]

url: https://opensource-demo.orangehrmlive.com/
Username : Admin | Password : admin123
"""
from selenium import webdriver
import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from Selenium.POMProjectDemo.Pages.loginPage import LoginPage
from Selenium.POMProjectDemo.Pages.homePage import HomePage
import HtmlTestRunner


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_login_valid(self):

        driver = self.driver

        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

        time.sleep(2)

    def test_02_login_invalid_username(self):

        driver = self.driver

        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin1")
        login.enter_password("admin123")
        login.click_login()
        message = login.check_invalid_username_message()
        # print(message)
        self.assertEqual(message, "Invalid credentials")

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed!!!")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/Ray/PycharmProjects/webclawler/Reports"))

