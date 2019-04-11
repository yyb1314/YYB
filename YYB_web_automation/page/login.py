# -*- coding: utf-8 -*-
from common.basepage import Base
import unittest
class Login(Base):
    loc1 = ("id","account")
    loc2 = ("name","password")
    loc3 = ("id","submit")
    loc4 = ("id","userMenu")
    text = "admin"
    def loginpage(self,user = "admin",pswd = "123456"):
        """登录"""
        self.sendkeys(self.loc1,user)
        self.sendkeys(self.loc2,pswd)
        self.click(self.loc3)
    def duanyan(self):
        """断言"""
        self.result = self.is_text_to_be_present_in_element(self.loc4,self.text)
        return self.result
    def isalert(self):
        """判断是否有alera弹框"""
        # self.alert = self.is_alert_is_present()
        # if self.alert == False:
        #     return False
        # else:
        #     alert = self.alert.text
        #     self.alert.accept()
        #     return alert
        try:
            a = self.driver.switch_to_alert()
            text = a.text
            a.accept()
            return text
        except:
            return ""
if __name__ == "__main__":
     unittest.main()

