# coding : utf-8
from page.login import Login
from page.add_day2_page import Add_project
from selenium import webdriver
import unittest
class TestF(unittest.TestCase):
    """测试禅道添加一个项目的用例"""
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.linken = Add_project(cls.driver)
        cls.linken1 = Login(cls.driver)
    def test_01(self):
        self.linken1.loginpage()
        self.linken.add_project()
        lk = self.linken.add_project_duanyn()
        print(lk)
        self.assertTrue(lk)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__ == "__main__":
    unittest.main()
