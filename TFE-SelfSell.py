"""
*** 修改程式碼前，請先在 TFE-QA-SelfSell.py 進行
scope: 檢查投資/借貸 頁面主動拍賣區的拍賣金額是否異常
- 以 windows 工作排程器，每五分鐘執行一次
- 檢查結果寫入 Bid_check.log

Date: 2019-05-29
"""
import requests
from bs4 import BeautifulSoup
import datetime
import smtplib
from email.mime.text import MIMEText

# 取得目前時間
theTime = datetime.datetime.now()

# URL 測試區
# url = 'http://172.31.1.103/TFEFrontend/product/productList'
# URL 正式區
url = "https://www.taiwanfundexchange.com.tw/TFEFrontend/product/productList"
res = requests.get(url)

# print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')

# 擷取主動拍賣區 的 script code
proactivlies = soup.find("ul", id="sellact").select("script")

# 判斷是否有 擷取到主動拍賣的資料
if len(proactivlies) == 0:
    print(theTime)
else:
    i = 0
    print(theTime, "有主動拍賣紀錄，共", len(proactivlies), "筆")
    for act in proactivlies:
        i += 1
        # print(act.text) 結果如下:
        # showBidSell("sellact1", '1905133743', '900', '1000', '2', '25', '1000', '', '10', 0, "/TFEFrontend/product/detail?from=auction&shelId=1905133743", "buySellactItem(1905133743, 'L122807174', 2, 900)");

        actList = act.text.replace(" ", "").replace("'", "").split(",")
        # 主動拍賣 判斷價格是否異常: 正常拍賣金額最高限額為 ((目前期數-1)* 每期標金) * 0.9
        normalPrice = ((int(actList[4])-1) * int(actList[3])) * 0.9
        # print("Normal price: ", normalPrice)
        if int(actList[2]) > normalPrice:
            myContent = str(theTime) + " " + "[第 " + str(i) + " 筆拍賣] 競標組合:" + actList[1] + " 每期金額:" + actList[3] + " 拍賣金額:" + actList[2] + " !!! 拍賣金額異常 !!!"
            print(myContent)

            # print("競標組合:", actList[1])
            # print("每期金額:", actList[3])
            # print("期數: ", actList[4] + " of " + actList[5])
            # print("拍賣金額:", int(actList[2]))
            # print("!!! 標金異常 !!!")
            # print("----------------------")

            # ============= 寄出郵件通知 ===================
            try:
                gmail_user = 'shacom.mantis@gmail.com'
                gmail_password = 'Pass@001'  # your gmail password

                msg = MIMEText(myContent)
                msg['Subject'] = '工作排程 - 檢查主動拍賣金額發現異常'
                msg['From'] = gmail_user
                msg['To'] = 'raytsao@shacom.com.tw'
                msg['Cc'] = 'jonaschang@shacom.com.tw'

                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.ehlo()
                server.login(gmail_user, gmail_password)
                server.send_message(msg)
                server.quit()

                print("==== Email sent! ====")

            except smtplib.SMTPException:
                print("Error sending message!!")

