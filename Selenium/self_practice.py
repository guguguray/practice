"""
https://opensource-demo.orangehrmlive.com/
Username : Admin | Password : admin123
"""
from selenium import webdriver
import time
import unittest

url = "https://opensource-demo.orangehrmlive.com/"


class LoginLogoutTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome()
        cls.browser.implicitly_wait(5)
        cls.browser.maximize_window()

    def test_case01_login(self):
        self.browser.get(url)
        self.browser.find_element_by_id("txtUsername").send_keys("Admin")
        self.browser.find_element_by_id("txtPassword").send_keys("admin123")
        self.browser.find_element_by_id("btnLogin").click()

    def test_case02_logout(self):
        self.browser.find_element_by_id("welcome").click()
        self.browser.find_element_by_link_text("Logout").click()
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.browser.quit()
        print("Test Completed!!!")
