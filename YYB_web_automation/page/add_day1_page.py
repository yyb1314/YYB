# coding : utf-8
from common.base_package import Base
import time
import unittest
'''
测试禅道添加一个产品的功能
1、启动浏览器输入登录的url
2、登录禅道
3、点击页面产品按钮
4、点击页面添加产品按钮
5、输入需要添加产品的详细信息
6、保存添加的信息
7、判断是否添加成功
8、退去浏览器
'''
# 定位器1
loc_product = ("link text","产品")
loc_add_product = ("xpath","//*[@class='nav']/li[11]")
loc_product_name = ("name","name")
loc_product_id = ("name","code")
loc_test_leader = ("xpath","//*[@id='QD_chosen']/a")
loc_test_leader_add = ("xpath","//*[@id='QD_chosen']/div/ul/li")
loc_publishing_officer = ("xpath","//*[@id='RD_chosen']/a")
loc_publishing_officer_add = ("xpath","//*[@id='RD_chosen']/div/ul/li")
iframeclass = "ke-edit-iframe" # 用js切换iframe
loc_preservation = ("xpath","//*[@id='submit'and @type='submit']")
# 定位器2
loc_add_productnew = ("xpath","//*[@class='nav']/li[12]")
loc1 = ("xpath","//*[@id='productList']/tbody/tr[1]/td[1]/input")
loc_preservationnew = ("xpath","//*[@id='submit'and @type='submit']")
loc_lk = ("xpath","//*[@class='outer']/form/table/tbody/tr[1]/td[8]/select")
loc_li = ("xpath","//*[@class='outer']/form/table/tbody/tr[1]/td[8]/select/option[3]")
loc_preservationnew1 = ("xpath","//*[@id='submit'and @type='submit']")
loc_text = ("xpath","//*[@id='productList']/tbody/tr[1]/td[2]/a")
# 断言
loc_duanyan = ("xpath","//*[@class='panel-heading nobr']/strong")
timenew = time.strftime("%Y_%m_%d_%H_%M_%S")
# 测试时添加的数据
text1 = "联通_VOLTE" + timenew
text2 = "VOLTE" + timenew
text3 = "外场测试" + timenew
class Add_product(Base):
    """添加一个产品"""
    def add_product(self):
        """添加产品的信息"""
        self.click(loc_product)
        self.click(loc_add_product)
        self.sendkeys(loc_product_name,text1)
        self.sendkeys(loc_product_id,text2)
        self.click(loc_test_leader)
        self.click(loc_test_leader_add)
        self.click(loc_publishing_officer)
        self.click(loc_publishing_officer_add)
        self.js_iframe_class(iframeclass,text3)
        self.js_focus(loc_preservation)
        self.click(loc_preservation)
    def add_productnew(self):
        """删除产品的信息"""
        self.click(loc_product)
        self.click(loc_add_productnew)
        self.lk = self.is_text(loc_text)
        self.click(loc1)
        self.click(loc_preservationnew)
        self.click(loc_lk)
        self.click(loc_li)
        self.click(loc_preservationnew1)
    def add_produt_duanyan(self):
        """判断是否添加成功"""
        result = self.is_text_to_be_present_in_element(loc_duanyan,text1)
        return result
    def add_produt_duanyannew(self):
        """判断是否删除成功"""
        result = self.is_text_to_be_present_in_element(loc_text,self.lk)
        return result
if __name__ == "__main__":
    unittest.main()
    # from page.login import Login
    # from selenium import webdriver
    # driver = webdriver.Firefox()
    # linken = Add_product(driver)
    # linken1 = Login(driver)
    # linken1.loginpage()
    # linken.add_product()
    # lk = linken.add_produt_duanyan()
    # print(lk)
















