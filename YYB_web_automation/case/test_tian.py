# coding : utf-8
from page.tiandiweiye_page import TianDiWeiYe
from selenium import webdriver
import unittest
class  TestA(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome() # 启动浏览器
        self.linken = TianDiWeiYe(self.driver) # 实例化参数
        self.linken.max_window() # 全屏
    def test_01(self):
        self.linken.driver_get() # 打开url
        self.linken.tiandi() # 点点点
        result = self.linken.tiandi_duanyan() # 实际结果
        print(result)
        self.assertTrue(result) # 断言
    def tearDown(self):
        self.linken.driver_quit()
if __name__ == '__main__':
    unittest.main()