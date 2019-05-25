# -*- coding: utf-8 -*-
from selenium import webdriver
from page.login import Login
import unittest
text1 = "admin"
text2 = "170407"
text3 = "admin1"
text4 = ""
class TestE(unittest.TestCase):
    """登录案例"""
    def setUp(self):
         self.linken.isalert()
         self.driver.get("http://localhost/zentao/user-login-L3plbnRhby8=.html")
         self.driver.delete_all_cookies()  # 退去登录
         self.driver.refresh()
    def test_01(self):
        """输入正确账号密码登录"""
        self.linken.loginpage()
        result = self.linken.duanyan()
        self.assertTrue(result)
        print("登录成功")
    def test_02(self):
        """输入错误账号密码登录"""
        self.linken.loginpage(text1,text2)
        result = self.linken.duanyan()
        self.assertFalse(result)
        print("登录失败")
    def test_03(self):
        """输入错误账号密码登录"""
        self.linken.loginpage(text3,text4)
        result = self.linken.duanyan()
        self.assertFalse(result)
        print("登录失败")
    def test_04(self):
        """输入正确账号密码登录"""
        self.linken.loginpage()
        result = self.linken.duanyan()
        self.assertTrue(result)
        print("登录成功")
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.linken = Login(cls.driver)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__ == "__main__":
    unittest.main()