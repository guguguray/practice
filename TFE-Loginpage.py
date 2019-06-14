"""
Login page  with 辨識驗證碼轉文字，登入 TFE
Notes: TFE 測試 site 驗證碼機制是假的，未判斷驗證碼正確性
"""

from selenium import webdriver
from PIL import Image, ImageEnhance
from selenium.webdriver.common.keys import Keys
import time
import pytesseract


def binaryzation(threshold=150):  # 降噪，圖片二值化
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)

    return table

# initial variable
fId = "A118581748"
fAcc = "tester2"
fPwd = "tester2"
code = ""

url = "http://172.31.1.103/TFEFrontend/Servicelogin?NeedCheck=0"

# driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get(url)
orgUrl = driver.current_url


# close Advertisement
# driver.find_element_by_id("btnCloseAdModal").click()

# findloginlink = driver.find_elements_by_tag_name('a')
# for e in findloginlink:
#     if e.get_attribute("onclick") == "CheckAgentBeforeLogin()":
#         e.click()

driver.implicitly_wait(30)
driver.find_element_by_id("identityid_login").clear()
driver.find_element_by_id("identityid_login").send_keys(fId)
driver.find_element_by_id("loginAccount_login").clear()
driver.find_element_by_id("loginAccount_login").send_keys(fAcc)
driver.find_element_by_id("password_login").clear()
driver.find_element_by_id("password_login").send_keys(fPwd)

# 辨識驗證碼 直到 取得辨識後的文字
while True:
    if code.strip() != "" and len(code) == 4:
        driver.find_element_by_id("verifycode_login").clear()
        driver.find_element_by_id("verifycode_login").send_keys(code)
        driver.find_element_by_id("sendButton").click()

        # 檢查目前網頁抬頭是否是原來的網頁的抬頭，因為原來的網頁才有驗證碼錯誤的定位元素
        # 如進入不同的頁面，就會出現"找不到定位元素" 的錯誤訊息
        if driver.current_url == orgUrl:
            # 找尋驗證碼錯誤的訊息
            fError = driver.find_element_by_xpath("//p[contains(text(), '驗證碼')]")
            print("找尋元素:", fError)

            # 檢查驗證碼有誤時
            if fError:
                time.sleep(2)
                print("驗證碼比對錯誤，畫面回到上方，重新產生驗證碼")
                # 關閉驗證碼有誤的錯誤訊息
                driver.find_element_by_xpath("//i[@class='fa fa-times-circle']").click()
                # 清除驗證碼欄位內容
                driver.find_element_by_id("verifycode_login").clear()
                code = ""
                # 控制畫面回上端
                driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        else:
            print("登入成功")
            time.sleep(1)
            break
    else:
        # time.sleep(2)
        # 點擊重新產生驗證碼
        driver.find_element_by_xpath("//i[@class='fa fa-refresh']").click()

        # 擷取取登入畫面
        driver.get_screenshot_as_file('login-screenshot.png')

        img_code = driver.find_element_by_xpath("//span[@class='verifycode-wrap']//img[@id='verifyImg']")
        time.sleep(1)

        # 算出驗證碼的四個點，即驗證碼四個角的座標地址
        left = img_code.location['x']
        top = img_code.location['y']
        right = img_code.location['x'] + img_code.size['width']
        bottom = img_code.location['y'] + img_code.size['height']
        print("驗證碼座標::", left, top, right, bottom)
        # 利用python的PIL圖片處理庫，利用座標，切出驗證碼的圖
        im = Image.open('login-screenshot.png')
        im = im.crop((left, top, right, bottom))
        im.save('code.png')

        im = im.convert('L')
        # im.show()
        im = im.point(binaryzation(), '1')  # 二值化
        # im.show()
        im.save('code.png')

        # sharpness = ImageEnhance.Contrast(im)  # 對比度增强
        # sharp_img = sharpness.enhance(5.0)
        # sharp_img.save("code.png")
        # sharp_img.show()

        time.sleep(1)

        # 打開驗證碼 code.png
        img = Image.open('code.png')
        # 利用 pytesseract 識別碼
        # -psm 8 為識別模式
        # -c tessedit_char_whitelist=1234567890  的意思是 識別純數字(0-9)
        code = pytesseract.image_to_string(img, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
        if code.strip() == "":
            print("驗證碼:: 無法識別")
        else:
            print('驗證碼:: {}'.format(code))

print("driver close")
driver.close()
driver.quit()