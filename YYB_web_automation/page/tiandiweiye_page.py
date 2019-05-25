# coding : utf-8
from common.base_package import Base
# 定位器
loc1 = ("link text","产品中心")
loc2 = ("link text","半球网络摄像机")
loc3 = ("css selector","#menu-item-19020>a")
loc4 = ("css selector",".breadcrumb>span>span")
class TianDiWeiYe(Base):
    def tiandi(self):
        self.mouse(loc1)
        self.click(loc2)
        self.click(loc3)
    def tiandi_duanyan(self):
        try:
            result = self.is_text(loc4)
            newresult = self.is_text_to_be_present_in_element(loc4,result)
            return newresult
        except:
            return False
if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Firefox()
    linken = TianDiWeiYe(driver)
    linken.max_window()
    linken.driver_get()
    linken.tiandi()
    lk = linken.tiandi_duanyan()
    print(lk)