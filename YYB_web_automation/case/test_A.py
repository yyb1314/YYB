# -*- coding: utf-8 -*-
from page.bug_jjie_page import Bug_jie
from page.zentaopage import LoginBug
from selenium import  webdriver
import unittest
loc10 = ("xpath","//*[@id='bugList']/tbody/tr[1]/td[4]/span")
loc12 = ("xpath","//*[@id='bugList']/tbody/tr[1]/td[4]/a")
class TestD(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.linken = Bug_jie(cls.driver)
        cls.linken1 = LoginBug(cls.driver)
        cls.linken1.loginpage(user="admin",pswd="123456")
    def test_01(self):
        self.linken.gunbi()
        lk1 = self.linken.findelement(loc10).text
        print(lk1)
        result = self.linken.duanyango(lk1)
        print(result)
        self.assertTrue(result)
    def test_02(self):
        self.linken.Bug_jia()
        lk = self.linken.findelement(loc12).text
        print(lk)
        result = self.linken.duanyangi(lk)
        print(result)
        self.assertTrue(result)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__ == "__main__":
    unittest.main()

