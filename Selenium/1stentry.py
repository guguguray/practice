#coding = utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


url = "https://www.baidu.com/"

# Creat chrome instance
driver = webdriver.Chrome()

# startup chrome and navigate to url
driver.get(url)

# 檢查確認 title 是否包含 百度一下
assert "百度一下" in driver.title

# 定位輸入欄位名稱:  name = "wd"
input_text = driver.find_element_by_name("wd")

# 清空輸入欄位 "wd" 的內容, 輸入文字後 按下Enter
input_text.clear()
input_text.send_keys("selenium")
input_text.send_keys(Keys.RETURN)

# 檢查確認 "No results found" 不在原始頁面碼中
assert "No results found." not in driver.page_source

# Close browser
driver.close()
