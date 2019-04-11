# -*- coding: utf-8 -*-
from common.basepage import Base
import time
import unittest

loc1 = ("link text","测试")
loc2 = ("link text","用例")
loc3 = ("link text","建用例")
loc4 = ("css selector",".chosen-choices")
loc5 = ("xpath","//div[@id='stage_chosen']/div/ul/li[2]")
loc6 = ("id","title")
loc7 = ("id","precondition")
loc8 = ("id","steps[]")
loc9 = ("id","expects[]")
loc10 = ("id","keywords")
loc11 = ("name","labels[]")
loc12 = ("id","submit")
loc13 = ("xpath","//*[@id='caseList']/tbody/tr/td[3]/a")

timestr = time.strftime("%Y_%m_%d_%H_%M_%S")
text1 = "DTMF语音" + timestr
text2 = "终端插入联通SIM卡"
text3 = "终端拨打12580，根据语音提示操作"
text4 = "终端能拨通号码，根据语音提示能正确响应DTMF指令"
text5 = "DTMF"
text6 = "联通外场"

class Add_yli(Base):
    def xinzenyli(self):
        self.click(loc1)
        self.click(loc2)
        self.click(loc3)
        self.click(loc4)
        self.click(loc5)
        self.sendkeys(loc6,text1)
        self.sendkeys(loc7,text2)
        self.sendkeys(loc8,text3)
        self.sendkeys(loc9,text4)
        self.sendkeys(loc10,text5)
        self.sendkeys(loc11,text6)
        self.click(loc12)
    def duanyan(self):
        self.result = self.is_text_to_be_present_in_element(loc13,text1)
        return self.result
if __name__ == "__main__":
     unittest.main()
