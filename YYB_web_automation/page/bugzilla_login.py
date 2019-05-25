# coding : utf-8
from common.base_package import Base
'''
测试bugzilla登录功能
1、点击登入
2、输入账号 密码
3、点击登入
4、判断登录是否成功
'''
# 定位器
loc1 = ("id","login_link_top") # 登入
loc2 = ("class name","bz_login") # 账号
loc3 = ("class name","bz_password") # 密码
loc4 = ("name","GoAheadAndLogIn") # 登入
loc5 = ("link text","管理者介面") # 管理者介面
class Bugzilla_login(Base):
    def login(self,user="shanghai@etest.com",pswd="etest@1234"):
        self.driver_get()
        self.click(loc1)
        self.sendkeys(loc2,user)
        self.sendkeys(loc3,pswd)
        self.click(loc4)
    def login_duanyan(self):
        try:
            result = self.is_text(loc5)
            resultnew = self.is_text_to_be_present_in_element(loc5,result)
            return resultnew
        except:
            return False
# if __name__ == '__main__':
#     from selenium import webdriver
#     driver = webdriver.Firefox()
#     linken = Bugzilla_login(driver)
#     linken.max_window()
#     linken.login()
#     linken.login_duanyan()
#     linken.driver_quit()

