# -*- coding: utf-8 -*-
from selenium import webdriver
from page.zentaopage import LoginBug
import unittest
loc15 = ("xpath","//*[@id='bugList']/tbody/tr[1]/td[4]/a")
class TestB(unittest.TestCase):
    """添加bug案例"""
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.linken = LoginBug(cls.driver)
        cls.linken.loginpage(user="admin",pswd="123456")
    def test_01(self):
        """输入正确账号密码登录"""
        self.linken.loginadd()
        result = self.linken.duanyan()
        self.assertTrue(result)
        lk = self.linken.findelement(loc15).text
        print(lk)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__ == "__main__":
    unittest.main()