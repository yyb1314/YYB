# -*- coding: utf-8 -*-
from selenium import webdriver
from page.add_yli_page import Add_yli
from page.zentaopage import LoginBug
import unittest
loc13 = ("xpath","//*[@id='caseList']/tbody/tr/td[3]/a")
class TestC(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Ie()
        cls.driver.maximize_window() # 全屏显示
        cls.linken = Add_yli(cls.driver)
        cls.linkenl = LoginBug(cls.driver)
        cls.linkenl.loginpage(user="admin",pswd="123456")
    def test_01(self):
        self.linken.xinzenyli()
        lk = self.linken.findelement(loc13).text
        print(lk)
        result = self.linken.duanyan()
        print(result)
        self.assertTrue(result)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
