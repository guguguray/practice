import smtplib
from email.mime.text import MIMEText

try:
    gmail_user = 'shacom.mantis@gmail.com'
    gmail_password = 'Pass@001'  # your gmail password

    msg = MIMEText('Test Send Mail through Gmail')
    msg['Subject'] = 'test send mail '
    msg['From'] = gmail_user
    msg['To'] = 'raytsao@shacom.com.tw'
    msg['Cc'] = ''

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.send_message(msg)
    server.quit()

    print('==== Email sent! ====')

except smtplib.SMTPException:
    print("Error sending message!!")