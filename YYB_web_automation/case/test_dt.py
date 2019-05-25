# -*- coding: utf-8 -*-
from selenium import webdriver
from common.read_excel import ExcelUtil
from page.zentaopage import LoginBug
from page.login import Login
import os
import unittest
import ddt
#用excle表格传入
propath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
print(propath)
filepath = os.path.join(propath,"common","data_excel.xlsx")
print(filepath)
data = ExcelUtil(filepath)
datadict = data.dict_data()
print (datadict)
@ddt.ddt
class TestE(unittest.TestCase):
    """登录页面测试案例"""
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.linken = LoginBug(self.driver)
        self.linken1 = Login(self.driver)
        self.linken.is_alert()
        self.driver.delete_all_cookies()
        self.driver.refresh()
    def login_case(self,user,pswd,expect):
        """登录流程"""
        self.linken.loginpage(user,pswd)
        result = self.linken1.duanyan()
        print(result)
        if expect == "True": expectnew = True
        else:expectnew = False
        print(expect)
        self.assertEqual(result,expectnew)
    @ddt.data(*datadict)
    def test_01(self,data):
        self.login_case(data["user"],data["pswd"],data["expect"])
    def tearDown(self):
        self.driver.quit()
if __name__ == "__main__":
    unittest.main()