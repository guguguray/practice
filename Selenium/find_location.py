from selenium import webdriver
import os

"""
grep source from: hello.html
- find element by
- find elements by

*** Better to find element order:
    1. id
    2. class
    3. css selector
*** find by xpath: do not use absolute path
"""
# Create Chrome instance
driver = webdriver.Chrome()

# get from local html page
file_path = 'file:///' + os.path.abspath('hello.html')
driver.get(file_path)

# find name by class
head_title = driver.find_element_by_class_name("head_title")
print("Find by class: " + head_title.text)

# find by id
world = driver.find_element_by_id("world")
print("find by id: " + world.text)

# find by name
username = driver.find_element_by_name("username")
print("find by name: " + username.get_attribute("value"))

# find by tag name
submit_btn = driver.find_element_by_tag_name("button")
print("find by tag: " + submit_btn.text)

# find by link
kancloud = driver.find_element_by_partial_link_text("看雲首頁")
print("find by link: " + kancloud.get_attribute("href"))

# find by xpath
username = driver.find_element_by_xpath("//body/div/input")
print("find by xpath-username: " + username.get_attribute("value"))

password = driver.find_element_by_xpath("//input[@name='password']")
print("find by xpath-pwd: " + password.get_attribute("value"))

password = driver.find_element_by_xpath("//input[@name='password'][@type='text']")
print(password.get_attribute("value"))

# find by css + input name
username = driver.find_element_by_css_selector("input[name='username")
print("find by css-username with inputname: " + username.get_attribute("value"))

# find by css + class name
username = driver.find_element_by_css_selector("input.user_name")
print("find by css-username with classname: " + username.get_attribute("value"))

# find by css + multiple class name
password = driver.find_element_by_css_selector("input.ptqa.pwd")
print("find by css-pwd with Multi classname(input.ptqa.pwd): " + password.get_attribute("value"))

# find by css + level class name
password = driver.find_element_by_css_selector(".login .ptqa.pwd")
print("find by css-pwd with level classname(.login .ptqa.pwd): " + password.get_attribute("value"))

# find by css + level class name with target inputname
password = driver.find_element_by_css_selector(".login .ptqa[name='password']")
print("find by css-(.login .ptqa[name='password']): " + password.get_attribute("value"))

# find by css + level class name with parent child
password = driver.find_element_by_css_selector("div[id='login_form']>input[name='password']")
print("find by css-(div[id='login_form']>input[name='password']): " + password.get_attribute("value"))

# Manipulate with select box
selectname = driver.find_element_by_class_name("city").find_element_by_css_selector("option[value='mm']")
print("Select box: find by css: " + selectname.text)

print("-"*20)
# grep multiple option by using find_element(s) >>> find_elements_by_css_selector()
cities = driver.find_elements_by_css_selector(".city option")
print(type(cities))
for city in cities:
    print(city.text)



#Close Chrome
driver.close()
