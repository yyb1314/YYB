# -*- coding: utf-8 -*-
from page.lkio_page import Linken
from page.zentaopage import LoginBug
from selenium import  webdriver
import unittest
class TestD(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Ie()
        cls.driver.maximize_window()
        cls.linken = Linken(cls.driver)
        cls.linken1 = LoginBug(cls.driver)
        cls.linken1.loginpage(user="admin",pswd="123456")
    def test_01(self):
        a = self.linken.lklo()
        b = self.linken.duanyanju()
        print(a,b)
        self.assertNotEqual(a,b)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__ == "__main__":
    unittest.main()
