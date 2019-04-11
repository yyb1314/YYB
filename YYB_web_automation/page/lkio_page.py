# -*- coding: utf-8 -*-
from common.basepage import Base
import time

loc1 = ("xpath","//*[@id='block7']/div[2]/table/tbody/tr[1]/td[3]")
loc2 = ("xpath","//*[@id='titlebar']/div[2]/div[2]/a[4]/i")

class Linken(Base):
    def lklo(self):
        time.sleep(1)
        # self.js_scroll_end()
        self.lk = self.is_text(loc1)
        self.click(loc1)
        self.click(loc2)
        self.is_alert()
        time.sleep(1)
        self.driver.refresh()
        # self.js_scroll_end()
        return self.lk
    def duanyanju(self):
        self.lk1= self.is_text(loc1)
        return self.lk1

