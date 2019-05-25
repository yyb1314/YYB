# -*- coding: utf-8 -*-
from common.base_package import Base
loc1 = ("link text","测试")
loc2 = ("link text","用例")
loc3 = ("xpath","//*[@id='caseList']/tbody/tr[1]/td[13]/a[5]/i")
loc4 = ("xpath","//*[@id='caseList']/tbody/tr[1]/td[3]/a")

class Remove(Base):
    """删除一条测试用例"""
    def icon_remove(self):
        """进入删除"""
        self.click(loc1)
        self.click(loc2)
        self.lk = self.is_text(loc4)
        self.click(loc3)
    def isalert(self):
        """判断是否有alera弹框"""
        self.alert = self.is_alert_is_present()
        if self.alert == False:
            return False
        else:
            alert = self.alert.text
            self.alert.accept()
            return alert
    def duanyanyu(self):
        """断言"""
        self.driver.refresh()
        result = self.is_text_to_be_present_in_element(loc4,self.lk)
        return result





