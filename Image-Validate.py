from PIL import Image, ImageEnhance
from selenium import webdriver
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

url = 'http://172.31.3.103/TFEFrontend/Servicelogin?NeedCheck=0'
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get(url)

code = ''

while True:
    if code.strip() != '':
        break
    else:
        # time.sleep(2)
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
        # code = pytesseract.image_to_string(img, config='-psm 8 -c tessedit_char_whitelist=1234567890')
        code = pytesseract.image_to_string(img, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
        print('驗證碼識別:: {}'.format(code))


# 關閉 driver
driver.close()

