#!/usr/bin/env python
# coding: utf-8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header


sender = '78563943@163.com'
receiver = '83472848@qq.com'
subject = 'python email test'
smtpserver = 'smtp.163.com'
username = '78563943@163.com'
password = 'xxxxxx'
#中文需参数‘utf-8’，单字节字符不需要
content = 'hello'

msg = MIMEMultipart()
msg.attach(MIMEText(content, _subtype='html', _charset='utf-8',))

msg['Subject'] = Header('hhahahhaha', 'utf-8')
msg['From'] = sender
msg['To'] =  receiver

smtp = smtplib.SMTP()
smtp.connect('smtp.163.com')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.close()
