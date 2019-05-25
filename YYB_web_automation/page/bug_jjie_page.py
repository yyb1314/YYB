# -*- coding: utf-8 -*-
from common.base_package import Base
# 关闭一条bug
loc1 = ("link text","测试")
loc2 = ("link text","Bug")
loc3 = ("xpath","//*[@id='bugList']/tbody/tr[1]/td[12]/a[3]/i")
# 需要切换iframe
loc4 = ("id","resolution")
value1="notrepro"
loc5 = ("xpath","//*[@id='resolvedBuild_chosen']/a")
loc6 =("css selector",".active-result.highlighted")
loc7 = ("name","labels[]")
loc8 =("css selector",".ke-edit")
loc9 = ("id","submit")
loc10 = ("xpath","//*[@id='bugList']/tbody/tr[1]/td[4]/span")
loc11 = ("xpath","//*[@id='bugList']/tbody/tr[1]/td[12]/a[2]/i")
# 需要切换iframe
loc12 = ("xpath","//*[@id='bugList']/tbody/tr[1]/td[4]/a")

text1 = "DTMF"
text2 = "林肯"

class Bug_jie(Base):
    def gunbi(self):
        self.click(loc1)
        self.click(loc2)
        self.click(loc3)
        self.driver.switch_to.frame(1)
        self.isselect(loc4,value1)
        self.click(loc5)
        self.click(loc6)
        self.sendkeys(loc7,text1)
        self.sendkeys(loc8,text2)
        self.click(loc9)
        self.driver.switch_to.default_content()
        self.driver.refresh()
    def Bug_jia(self):
        self.driver.refresh()
        self.click(loc11)
        self.driver.switch_to.frame(1)
        self.click(loc9)
        self.driver.switch_to.default_content()
    def duanyango(self,text):
        result = self.is_text_to_be_present_in_element(loc10,text)
        return result
    def duanyangi(self,text):
        result = self.is_text_to_be_present_in_element(loc12,text)
        return result



