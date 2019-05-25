# -*- coding: utf-8 -*-
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import smtplib
def send_mail(report_name,receiver = "2393392330@qq.com"):
    """
    发送测试报告到邮箱 以下已qq邮箱为例
    :param report_name: 需要发送的测试报告
    :param receiver: 邮件接收人
    :return:
    """
    # ----------------------------------------------------------
    # 获取邮件正文,读取测试报告的内容
    f = open(report_name, 'rb')
    mail_body = f.read()
    f.close()
    # 邮件服务器
    smtpserver = "smtp.qq.com"
    # 发件人和密码
    sender = '2393392330@qq.com'
    password = 'yiujprhtqfmjecai' # 此处填写SMTP授权登录码
    # 接收人
    # receiver = "**********@qq.com"  # 单人接收
    # receiver = ["*********@qq.com","**********@qq.com"] # 多人接收
    # 邮件主题
    subject = u'自动化测试报告'
    # ----------------------------------------------------------
    # 连接登录邮箱
    smtp=smtplib.SMTP()
    smtp.connect(smtpserver)
    # server = smtplib.SMTP(smtpserver,25)
    smtp.login(sender, password)
    # ----------------------------------------------------------
    # 添加附件
    sendfile = open(report_name, 'rb').read()
    att = MIMEText(sendfile, "base64", 'utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment;filename="test_report.html"'
    msg = MIMEMultipart('related')
    msgtext = MIMEText(mail_body, 'html', 'utf-8')
    msg.attach(msgtext)
    msg['From'] = sender
    if isinstance(receiver,str):
        msg['To'] = receiver # 单个收件人 str
    else:
        msg['To'] = ";".join(receiver) # 多人收件人 list
    msg['Subject'] = Header(subject, 'utf-8').encode()
    msg.attach(att)
    # ----------------------------------------------------------
    # 发送邮件
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print("测试报告电子邮件发送成功!")

# if __name__ == " __main__":
# send_mail(reportpath)
# SMTP授权登录码：yiujprhtqfmjecai