import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def Send_Mail():
    mail_host = 'smtp.163.com'
    receivers = ['1601664015@qq.com']  # 接受邮箱的人
    receiver = ';'.join(receivers)
    password = 'tl1995'  # 此处未邮箱授权码   为发送人的邮箱授权码
    sender = '18782048160@163.com'  # 发送邮箱的人

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = 'Python邮箱发送附件'

    # 邮箱正文
    msg.attach(MIMEText('测试发送文件', 'plain', 'utf-8'))

    # 构造附件2
    att2 = MIMEText(open('D:\\禅道\\Common\\Report\\zentao-Report.html', 'rb').read(), 'base64', 'utf-8')
    att2['Content-Type'] = 'application/octet-stream'
    att2['Content-Disposition'] = "attachment;filename='zentao-Report.html'"  # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    msg.attach(att2)

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)
        smtpObj.login(sender, password)
        smtpObj.sendmail(sender, receivers, msg.as_string())
        smtpObj.close()
        print('发送成功')
    except smtplib.SMTPException:
        print('无法发送')
