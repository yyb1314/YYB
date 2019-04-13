# -*- coding: utf-8 -*-
import unittest
import os
from common import HTMLTestRunner_cn
from common.send_mail import send_mail
# 获取该文件路径
curpath = os.path.dirname(os.path.realpath(__file__))
# 获取用例路径
casepath =os.path.join(curpath,"case")
lk = "test*.py"
discover =unittest.defaultTestLoader.discover(start_dir=casepath,pattern=lk)
print(discover)
# 生成HTML报告路径
reportpath= os.path.join(curpath,"report\\",) + "test_report.html"
# 打开报告写入内容
yb =open(reportpath,"wb")
runner = HTMLTestRunner_cn.HTMLTestRunner(stream=yb,
                                          title="可以装逼的测试报告",
                                          description="大佬好牛逼")
print("生成报告路径：%s"% reportpath)
# 调用add_case函数返回值
runner.run(discover)
# 发送测试报告到邮箱 调用函数
send_mail(reportpath)
yb.close()

