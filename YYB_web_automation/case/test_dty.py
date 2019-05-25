# -*- coding: utf-8 -*-
from page.add_move_page import Remove
from page.zentaopage import LoginBug
from selenium import  webdriver
import unittest
class TestD(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.linken = Remove(cls.driver)
        cls.linken1 = LoginBug(cls.driver)
        cls.linken1.loginpage(user="admin",pswd="123456")
    def test_01(self):
        self.linken.icon_remove()
        self.linken.isalert()
        result = self.linken.duanyanyu()
        print(result)
        self.assertFalse(result)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__ == "__main__":
    unittest.main()
