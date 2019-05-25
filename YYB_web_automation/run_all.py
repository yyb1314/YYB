# -*- coding: utf-8 -*-
import unittest
import time
import os
from common import HTMLTestRunner_cn
from common.send_mail import send_mail
# 获取当前脚本真实路径
curpath = os.path.dirname(os.path.realpath(__file__))
# 获取测试用例路径
casepath = os.path.join(curpath,"case")
discover = unittest.defaultTestLoader.discover(start_dir=casepath,
                                               pattern="test*.py",
                                               top_level_dir=None
                                               )
print(discover)
timenew = time.strftime("%Y_%m_%d_%H_%M_%S")
# 生成HTML报告的路径
reportpath = os.path.join(curpath,"report\\") + "%s_my_report.html" % timenew
# 打开报告写入内容
fp = open(reportpath,"wb")
runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                          title="测试报告的头部信息",
                                          description="测试报告的描述部分"
                                          )
print("生成报告路径：%s" % reportpath)
# 调用add_case函数返回值
runner.run(discover)
fp.close()
# 发送测试报告到邮箱 调用函数
# send_mail(reportpath)


