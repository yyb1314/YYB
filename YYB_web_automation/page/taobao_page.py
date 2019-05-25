# coding : utf-8
from common.base_package import Base
# 定位器
loc1 = ("link text","密码登录")
loc2 = ("id","TPL_username_1")
loc3 = ("id","TPL_password_1")
loc4 = ("id","J_SubmitStatic")
loc5 = ("xpath","//*[@class='site-nav-user']/a[1]")
# 文本
text1 = "yyb131455"
text2 = "woainiyb5201314!"
class Taobao(Base):
    def taobao(self):
        self.driver_get()
        self.click(loc1)
        self.sendkeys(loc2,text1)
        self.sendkeys(loc3,text2)
        self.click(loc4)
    def taobao_duanyan(self):
        result = self.is_text_to_be_present_in_element(loc5,text1)
        return result
if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Firefox()
    linken = Taobao(driver)
    linken.max_window()
    linken.taobao()
    r = linken.taobao_duanyan()
    print(r)
