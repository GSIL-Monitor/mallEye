#!/usr/bin/env python
# -- coding: utf-8 --
import unittest
import os
import HTMLTestRunner
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import smtplib

# 用例路径
case_path = os.path.join(os.getcwd(), "./")
# 报告存放路径
report_path = os.path.join(os.getcwd(), "./")


def all_case():
    discover = unittest.defaultTestLoader.discover(
        case_path, pattern="test04*.py", top_level_dir=None)
    return discover


def send_mail():
    smtpserver = "smtp.exmail.qq.com"
    user = "yuanzhifan@winshang.com"
    password = "YZF@dd9587"

    sender = 'yuanzhifan@winshang.com'
    receivers = ['yuanzhifan@winshang.com']
    # receivers = ['yuanzhifan@winshang.com', 'hexiaojuan@winshang.com']

    subject = 'mall眼自动化报告邮件'
    content = '<html><h3 style="color:red"></h3></html>'

    send_file = open(r"mall_report.html", 'rb').read()
    att = MIMEText(send_file, 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment;filename = "mall_report.html"'

    msgRoot = MIMEMultipart()
    msgRoot.attach(MIMEText(content, 'html', 'utf-8'))
    msgRoot['subject'] = subject
    msgRoot['From'] = sender
    msgRoot['To'] = ','.join(receivers)
    msgRoot.attach(att)

    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    smtp.helo(smtpserver)
    smtp.ehlo(smtpserver)
    smtp.login(user, password)

    smtp.sendmail(sender, receivers, msgRoot.as_string())

    smtp.quit()


if __name__ == "__main__":
    report_path_html = os.path.join(report_path, "mall_report.html")
    fp = open(report_path_html, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'mall眼自动化测试报告',
                                           description=u'用例执行情况：')
    runner.run(all_case())
    fp.close()
    send_mail()


    # runner = unittest.TextTestRunner()
    # runner.run(all_case())
