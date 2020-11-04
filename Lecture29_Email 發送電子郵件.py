# 基本流程
'''
1. 使用 email.message 模組建立內容
2. 使用 smtplib 模組發送信件
3. 驗證寄件人身分 : 帳號密碼 / 兩階段驗證
'''

#----------------------------訊息物件----------------------------

'''
import email.message

# 建立訊息物件
msg = email.message.EmailMessage()

# 利用訊息物件建立基本設定
msg["From"] = "寄件人地址"
msg["To"] = "收件人地址"
msg["Subject"] = "電子郵件主題"
'''

#----------------------------純文字內容----------------------------

'''
msg.set_content("文字內容")
'''

#----------------------------HTML內容----------------------------

'''
msg.add_alternative("<h3>HTML 內容</h3>" , subtype = "html")
'''

#----------------------------發送信件----------------------------

'''
gmail 有其本身的 SMTP伺服器 用來發送電子郵件
'''

'''
import smtplib

# 連線 SMTP伺服器
# 可以從網路上 (gmail smtp sever) 找到主機名稱和連接埠號
sever = smtplib.SMTP_SSL("主機名稱" , 連接埠號)

# 驗證寄件人身分
# 根據連接的伺服器，輸入對應的帳號密碼
sever.login("帳號" , 密碼)

# 發送郵件
# msg 變數存放上一個步驟準備好的訊息物件
sever.send_message(msg)

# 發送完成後關閉連線
sever.close()
'''

#----------------------------Example----------------------------

import email.message
import smtplib

msg = email.message.EmailMessage()
msg["From"] = "kobe87020@gmail.com"
msg["To"] = "kobe87020@gmail.com"
msg["Subject"] = "Python 電子郵件 Test"

msg.set_content("Python Test")

sever = smtplib.SMTP_SSL("smtp.gmail.com" , 465)
sever.login("帳號" , "密碼")
sever.send_message(msg)

sever.close()