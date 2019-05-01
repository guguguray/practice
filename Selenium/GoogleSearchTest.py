"""
Small Sample Project: Unit Test, HTML Reports
Scope:
1. Create a test for Google Search
2. Add impilicit wait of 10 sec
3. Maximise windows
4. Create Unit Test
5. Add HTML reporting library
6. Run from command line (with/without) '-m unittest'
Troubleshoot:
問題: 滑鼠右鍵點擊: 只看到 Run: GoogleSearchTest... 執行後也無反映, testcase 無法運作
***因為是 unit test 所以應該要出現 Run: unittest in GoogleSearchTest...

解答: 因測試檔案放在新建的 Project中 , 應該是該 Project 設定環境有關
解決辦法 : 將檔案搬移到目前這個原首次建立的 Project 下 即可解決

"""
from selenium import webdriver
import unittest
import HtmlTestRunner

class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    # 1st test
    def test_search_automation(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Automation testing")
        self.driver.find_element_by_name("btnK").click()

    # 1st test
    def test_search_pythons_selenium(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("python selenium")
        self.driver.find_element_by_name("btnK1").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Complete!!")

# 要在 command-line 下 直接以 python 執行 不下參數 -m unittest 可加入以下程式碼
if __name__ == '__main__':
    # unittest.main()
    # 產生 html 報告  路徑的 \ 要改成 /
    unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output='C:/Users/Ray/PycharmProjects/webclawler/Reports'))