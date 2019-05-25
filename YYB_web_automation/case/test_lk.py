# coding ：utf-8
from selenium import webdriver
from page.bugzilla_login import Bugzilla_login
import unittest
class TestA(unittest.TestCase):
    """bugzilla登录功能测试"""
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.linken = Bugzilla_login(cls.driver)
        cls.linken.max_window()
    def test_01(self):
        """正确账号密码登录"""
        self.linken.login()
        result = self.linken.login_duanyan()
        print(result)
        self.assertTrue(result)
    def test_02(self):
        """错误账号密码登录"""
        self.linken.login("")
        result = self.linken.login_duanyan()
        print(result)
        self.assertFalse(result)
    @classmethod
    def tearDownClass(cls):
        cls.linken.driver_quit()
if __name__ == '__main__':
    unittest.main()