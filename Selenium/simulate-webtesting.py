"""
https://opensource-demo.orangehrmlive.com/
Username : Admin | Password : admin123
"""
from selenium import webdriver
import time
from selenium.webdriver import ActionChains


url = "https://opensource-demo.orangehrmlive.com/"

browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.maximize_window()

# Login
browser.get(url)
browser.find_element_by_id("txtUsername").clear()
browser.find_element_by_id("txtUsername").send_keys("Admin")
browser.find_element_by_id("txtPassword").send_keys("admin123")
browser.find_element_by_id("btnLogin").click()
verify_title = browser.find_element_by_css_selector(".box .head")
print(verify_title.text)


# Navigation Menu mouse hover
element = browser.find_element_by_xpath("//a[@id='menu_admin_viewAdminModule']")
actions = ActionChains(browser)
actions.move_to_element(element)
actions.perform()

element = browser.find_element_by_xpath("//a[@id='menu_admin_UserManagement']")
actions.move_to_element(element)
actions.perform()

browser.find_element_by_xpath("//a[@id='menu_admin_viewSystemUsers']").click()

time.sleep(5)

# Logout
browser.find_element_by_id("welcome").click()
browser.find_element_by_link_text("Logout").click()

time.sleep(3)

browser.close()
browser.quit()
print("Test Complete!!")




