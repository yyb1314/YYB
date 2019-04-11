# -*- coding: utf-8 -*-
import unittest
import os
from common import HTMLTestRunner_cn
curpath = os.path.dirname(os.path.realpath(__file__))
casepath =os.path.join(curpath,"case")
lk = "test*.py"
discover =unittest.defaultTestLoader.discover(start_dir=casepath,pattern=lk)
print(discover)
reportpath= os.path.join(curpath,"report\\",) + "test_report.html"
yb =open(reportpath,"wb")
print("生成报告路径：%s"% reportpath)
runner = HTMLTestRunner_cn.HTMLTestRunner(stream=yb,
                                          title="易测智能科技（天津）有限公司",
                                          description="中国联通外场测试")
runner.run(discover)

