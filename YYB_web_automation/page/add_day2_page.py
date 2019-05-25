# coding : utf-8
from common.base_package import Base
import time
'''
测试禅道添加一个项目的功能
1、启动浏览器输入登录的url
2、登录禅道
3、点击页面项目按钮
4、点击页面添加项目按钮
5、输入需要添加项目的详细信息
6、保存添加的信息
7、判断是否添加成功
8、退去浏览器
'''
# 定位器
loc1 = ("link text","项目")
loc2 = ("xpath","//*[@id='modulemenu']/ul/li[12]/a")
loc3 = ("name","name")
loc4 = ("name","code")
loc5 = ("name","end")
loc6 = ("name","team")
loc7 = ("css selector",".chosen-single.chosen-default")
loc8 = ("xpath","//*[@class='chosen-results']/li[1]")
iframe = "ke-edit-iframe" # 切换iframe
loc9 = ("id","submit")
loc10 = ("class name","close")
loc11 = ("xpath","//*[@class='panel-heading nobr']/strong") # 用来断言
# 需要的数据
timenew = time.strftime("%Y_%m_%d_%H_%M_%S")
text1 = "普通电信" + timenew
text2 = "无卡呼叫" + timenew
text3 = "2019-08-21"
text4 = "测试部" + timenew
text5 = "终端无卡状态，进行紧急号码呼叫，分别拨打110、120、119、112、122。"+ timenew
class Add_project(Base):
    def add_project(self):
        self.click(loc1)
        self.click(loc2)
        self.sendkeys(loc3,text1)
        self.sendkeys(loc4,text2)
        self.sendkeys(loc5,text3)
        self.sendkeys(loc6,text4)
        self.click(loc7)
        self.click(loc8)
        self.js_iframe_class(iframe,text5) # 切换iframe
        self.js_focus(loc9) # 聚焦到保存元素上
        self.click(loc9)
        lk = self.driver.window_handles # 获取所有的句柄 list类型
        self.driver.switch_to_window(lk[0]) # 切换到新弹出来的window
        self.click(loc10)
    def add_project_duanyn(self):
        result = self.is_text_to_be_present_in_element(loc11,text1)
        return result
# if __name__ == "__main__":
#     from selenium import webdriver
#     from page.login import Login
#     driver = webdriver.Firefox()
#     driver.maximize_window()
#     linken = Add_project(driver)
#     linken1 = Login(driver)
#     linken1.loginpage()
#     linken.add_project()
#     a = linken.add_project_duanyn()
#     print(a)
