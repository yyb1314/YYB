# coding : utf-8
from page.login import Login
from page.add_day1_page import Add_product
from selenium import webdriver
import unittest
class TestC(unittest.TestCase):
    """测试禅道添加一个产品的用例"""
    def test_01(self):
        self.linken1.loginpage()
        self.linken.add_product()
        lk = self.linken.add_produt_duanyan()
        print(lk)
        self.assertTrue(lk)
    def test_02(self):
        self.linken.add_productnew()
        lk = self.linken.add_produt_duanyan()
        print(lk)
        self.assertFalse(lk)
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.linken = Add_product(cls.driver)
        cls.linken1 = Login(cls.driver)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__ == "__main__":
    unittest.main()
