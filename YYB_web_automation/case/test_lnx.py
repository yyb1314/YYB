# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import unittest
class TestA(unittest.TestCase):
    """登录案例"""
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
    def setUp(self):
         self.isalert()
         self.driver.get("http://localhost/zentao/user-login-L3plbnRhby8=.html")
         self.driver.delete_all_cookies()  # 退去登录
         self.driver.refresh()
         time.sleep(1)
    def duanyan(self):
        """断言"""
        try:
            time.sleep(2)
            text = self.driver.find_element_by_id("userMenu").text
            return text
        except:
            return ""
    def isalert(self):
        """判断弹框是不是存在（Alera）"""
        try:
            time.sleep(1)
            a = self.driver.switch_to.alert
            textone = a.text
            a.accept()
            return textone
        except:
            return ""
    def test_01(self):
        """输入正确账号密码登录"""
        self.driver.find_element_by_id("account").send_keys("admin")
        self.driver.find_element_by_name("password").send_keys("123456")
        self.driver.find_element_by_id("submit").click()
        time.sleep(1)
        linken = self.duanyan()
        self.assertTrue(linken == "admin")
        print("登录成功")
    def test_02(self):
        """输入错误账号密码登录"""
        self.driver.find_element_by_id("account").send_keys("admin1")
        self.driver.find_element_by_name("password").send_keys("")
        self.driver.find_element_by_id("submit").click()
        time.sleep(1)
        linken = self.duanyan()
        self.assertTrue(linken == "")
        print("登录失败")
    def test_03(self):
        """输入错误账号密码登录"""
        self.driver.find_element_by_id("account").send_keys("admin")
        self.driver.find_element_by_name("password").send_keys("")
        self.driver.find_element_by_id("submit").click()
        time.sleep(1)
        linken = self.duanyan()
        self.assertTrue(linken == "")
        print("登录失败")
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__ == "__main__":
    unittest.main()
