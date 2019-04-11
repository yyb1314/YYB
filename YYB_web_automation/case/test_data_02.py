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
class Login_test(unittest.TestCase):
    """登录页面测试案例"""
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.linken = LoginBug(cls.driver)
        cls.linken1 = Login(cls.driver)
    def setUp(self):
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
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__=="__main__":
    unittest.main()