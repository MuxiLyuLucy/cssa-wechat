from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL

def send_mail(r_data,receiver):
    #qq邮箱smtp服务器
    host_server = 'smtp.qq.com'
    #sender_qq为发件人的qq号码
    sender_qq = '1730814337'
    #pwd为qq邮箱的授权码
    pwd = 'exsogcxfytgcccch'
    #发件人的邮箱
    sender_qq_mail = '1730814337@qq.com'
    #收件人邮箱
    #receiver = 'mchen160@jh.edu'
    #邮件的正文内容
    mail_content = '你好，JHU验证码为：' + str(r_data)
    #邮件标题
    mail_title = 'JHU验证码'

    #ssl登录
    smtp = SMTP_SSL(host_server)
    #set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
    smtp.set_debuglevel(1)
    smtp.ehlo(host_server)
    smtp.login(sender_qq, pwd)

    msg = MIMEText(mail_content, "plain", 'utf-8')
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender_qq_mail
    msg["To"] = receiver
    smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
    smtp.quit()

def send_e_main(r_data,receiver):
    try:
        send_mail(r_data,receiver)
        return True
    except:
        print("失败")

