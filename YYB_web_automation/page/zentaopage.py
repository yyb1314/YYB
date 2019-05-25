# -*- coding: utf-8 -*-
from common.base_package import Base
import time
import unittest
# 登录
loc1 = ("id","account")
loc2 = ("name","password")
loc3 = ("id","submit")
# 添加bug
loc4 = ("link text","测试")
loc5 = ("link text","Bug")
loc6 = ("link text","提Bug")
loc7 = ("xpath","//div[@id='openedBuild_chosen']/ul")
loc8 = ("xpath","//div[@id='openedBuild_chosen']/div/ul/li")
loc9 = ("css selector","#title")
# 需要切换iframe
loc20 = ("class name","ke-edit-iframe")
loc10 = ("class name","article-content")
loc13 = ("css selector","#submit")
# 断言
loc15 = ("xpath","//*[@id='bugList']/tbody/tr[1]/td[4]/a")
# 添加bug时需要的文本
timestr = time.strftime("%Y_%m_%d_%H_%M_%S")
text1 = "提交的bug" + timestr
text2 = "14567"
text3 = "227822"
text4 = "3337689"
text5 = "006"
# 登录网址
login_url = "http://localhost/zentao/user-login-L3plbnRhby8=.html"
class LoginBug(Base):
    def loginpage(self,user,pswd):
        """登录"""
        self.driver.get(login_url)
        self.sendkeys(loc1,user)
        self.sendkeys(loc2,pswd)
        self.click(loc3)
    def loginadd(self):
        """添加bug"""
        self.click(loc4)
        self.click(loc5)
        self.click(loc6)
        self.click(loc7)
        self.click(loc8)
        self.sendkeys(loc9,text1)
        self.frame = self.findelement(loc20)
        self.driver.switch_to.frame(self.frame)
        self.sendkeys(loc10,text2)
        self.driver.switch_to.default_content()
        self.click(loc13)
    def duanyan(self):
        """断言"""
        self.result = self.is_text_to_be_present_in_element(loc15,text1)
        return self.result
if __name__ == "__main__":
     unittest.main()

