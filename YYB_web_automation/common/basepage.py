# -*- coding: utf-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium import webdriver
class Base():
    """基于原生selenium做二次封装"""
    def __init__(self,driver:webdriver.Firefox):
        self.driver = driver
        self.timeout = 10
        self.poll = 0.5
    def findelement(self,locator):
        """查找单个元素,查找到返回元素对象，否则返回Timeout异常"""
        ele = WebDriverWait(self.driver,self.timeout,self.poll).until(lambda x: x.find_element(*locator))
        return ele
    def findelements(self,locator):
        """查找多个元素,查找到返回list对象，否则返回空[]"""
        try:
            eles = WebDriverWait(self.driver,self.timeout,self.poll).until(lambda x: x.find_elements(*locator))
            return eles
        except:
            return []
    def mouse(self,locator):
        """鼠标悬停操作"""
        ele = self.findelement(locator)
        ActionChains(self.driver).move_to_element(ele).perform()
    def sendkeys(self,locator,text):
        """输入文本"""
        ele = self.findelement(locator)
        ele.send_keys(text)
    def click(self,locator):
        """点击"""
        ele = self.findelement(locator)
        ele.click()
    def clear(self, locator):
        """清空"""
        ele = self.findelement(locator)
        ele.clear()
    def select_by_index(self,locator,index=0):
        """通过索引选择select下拉框，index是索引第几个，默认从0开始选择第一个"""
        ele = self.findelement(locator)
        Select(ele).select_by_index(index)
        ele.click()
    def isselect(self,locator,value):
        """通过value属性选择select下拉框"""
        ele = self.findelement(locator)
        Select(ele).select_by_value(value)
        ele.click()
    def select_by_text(self,locator,text):
        """通过文本属性定位选择"""
        ele = self.findelement(locator)
        Select(ele).select_by_visible_text(text)
        ele.click()
    def isselected(self,locator):
        """判断select下拉框是否被选中,返回bool值"""
        ele = self.findelement(locator)
        ele1 = ele.is_selected()
        return ele1
    def isdisplayed(self,locator):
        """判断元素是否显示，返回bool值"""
        ele = self.findelement(locator)
        ele1 = ele.is_displayed()
        return ele1
    def iselementsexist(self,locator):
        """判断元素是否存在，返回bool值"""
        ele = self.findelements(locator)
        n = len(ele)
        if n == 0:
            return False
        elif n == 1:
            return True
        else:
            print("定位到的元素个数：%s" %n)
            return True
    def is_title(self,title):
        """判断页面title文本是否与预期相符，返回bool值"""
        try:
            ele = WebDriverWait(self.driver,self.timeout,self.poll).until(EC.title_is(title))
            return ele
        except:
            return False
    def is_title_contains(self,title):
        """判断页面title文本是否是预期文本的片段，返回bool值"""
        try:
            ele = WebDriverWait(self.driver,self.timeout,self.poll).until(EC.title_contains(title))
            return ele
        except:
            return False
    def is_text_to_be_present_in_element(self,locator,text):
        """判断一个元素文本属性是否与预期相符，返回bool值"""
        try:
            ele = WebDriverWait(self.driver,self.timeout,self.poll).until(EC.text_to_be_present_in_element(locator,text))
            return ele
        except:
            return False
    def is_alert_is_present(self):
        """判断当前页面是否存在alert弹框,返回bool值"""
        try:
            ele = WebDriverWait(self.driver, 3, self.poll).until(EC.alert_is_present())
            return ele
        except:
            return False
    def is_alert(self):
        """处理页面alert弹框"""
        ele = self.is_alert_is_present()
        if ele == False:
            print("没有alert弹框")
        else:
            alert = ele.text
            ele.accept()
            return alert
    def is_text(self,locator):
        """获取元素文本属性"""
        try:
            ele = self.findelement(locator).text
            return ele
        except:
            return False
    def js_scroll_end(self):
       '''滚动到底部'''
       js_heig = "window.scrollTo(0, document.body.scrollHeight)"
       self.driver.execute_script(js_heig)
    def js_focus(self, loctor):
        '''聚焦元素'''
        target = self.findelement(loctor)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
    def js_scroll_top(self):
        '''回到顶部'''
        js = "window.scrollTo(0, 0)"
        self.driver.execute_script(js)
# if __name__ == "__main__":
#     from selenium import webdriver
#     driver = webdriver.Ie()
#     linken = Base(driver)
#     driver.get("https://www.cnblogs.com/yoyoketang/?_wv=1031")
#     loc1 = ("link text","下一页")
#     lki = linken.is_text(loc1)
#     print(lki)
#     lk = linken.findelement(loc1)
#     print(lk)
#     linken.click(loc1)

