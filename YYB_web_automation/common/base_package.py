# -*- coding: utf-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
class Base():
    """基于原生selenium做二次封装"""
    def __init__(self,driver:webdriver.Firefox): # driver:webdriver.Firefox：映射driver 为webdriver.Firefox
        self.driver = driver
        self.timeout = 10
        self.poll = 0.5
        self.url = "https://login.taobao.com/member/login.jhtml"
    def findelement(self,locator):
        """查找单个元素,查找到返回元素对象，否则返回Timeout异常 loctor 传元祖，如（"id", "kw"）"""
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
    def close(self):
        """关闭当前窗口"""
        self.driver.close()
    def back(self):
        """浏览器后退按钮"""
        self.driver.back()
    def forward(self):
        """浏览器前进按钮"""
        self.driver.forward()
    def refresh(self):
        """刷新"""
        self.driver.refresh()
    def driver_get(self):
        """打开url站点"""
        self.driver.get(self.url)
    def driver_quit(self):
        """关闭并停止浏览器服务"""
        self.driver.quit()
    def max_window(self):
        """窗口全屏"""
        self.driver.maximize_window()
    def window_size(self,w=1024,h=768):
        """设置窗口大小"""
        self.driver.set_window_size(w,h)
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
        """通过文本属性定位选择select下拉框"""
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
    def is_element_exist(self,locator):
        """判断元素是否存在，返回bool值"""
        try:
            ele = WebDriverWait(self.driver,self.timeout,self.poll).until(EC.presence_of_element_located(locator))
            return ele
        except:
            return False
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
        """判断一个元素文本属性是否与预期相符,返回bool值,text传预期文本"""
        try:
            ele = WebDriverWait(self.driver,5,self.poll).until(EC.text_to_be_present_in_element(locator,text))
            return ele
        except:
            return False
    def is_alert_is_present(self):
        """判断当前页面是否存在alert弹框,返回bool值"""
        try:
            ele = WebDriverWait(self.driver, 5, self.poll).until(EC.alert_is_present())
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
    def is_iframe(self,id_index_locator):
        """常规切换 iframe"""
        try:
            if isinstance(id_index_locator, int):  # 如果传入的是数字，则以该数字为下标取值
                self.driver.switch_to.frame(id_index_locator)
            elif isinstance(id_index_locator, str):  # 如果传入的是字符串，则用iframe名字取值
                self.driver.switch_to.frame(id_index_locator)
            elif isinstance(id_index_locator, tuple):  # 如果是元祖，则根据传入的locator取值
                ele = self.findelement(id_index_locator)
                self.driver.switch_to.frame(ele)
        except:
             print("iframe切换异常")
    def is_default_content(self):
        """跳出所有iframe,回到主界面"""
        self.driver.switch_to.default_content()
    def is_parent_frame(self):
        """返回上一级的iframe"""
        self.driver.switch_to.parent_frame()
    def is_all_handle(self):
        """获取所有窗口句柄，返回list"""
        all_handle = self.driver.window_handles
        return all_handle
    def switch_handle(self,n=-1):
        """n=-1默认切到新窗口，n=0责回到第一个窗口上"""
        new_handle = self.is_all_handle()
        self.driver.switch_to.window(new_handle[n])
    def js_click(self,classname):
        """js处理click失效问题"""
        js = 'document.getElementsByClassName("%s")[0].click();' % classname
        self.driver.execute_script(js)
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
    def js_iframe_id(self,iframeid,jstext):
        '''js切换iframe 通过定位iframe的id属性来完成 并输入文本'''
        js = 'document.getElementById("%s").contentWindow.document.body.innerHTML="%s"' %(iframeid,jstext)
        self.driver.execute_script(js)
    def js_iframe_class(self,iframeclass,jstext):
        '''js切换iframe 通过定位iframe的class属性来完成 并输入文本'''
        js = 'document.getElementsByClassName("%s")[0].contentWindow.document.body.innerHTML="%s"' %(iframeclass,jstext)
        self.driver.execute_script(js)
    def js_is_readonly(self,calendar,date):
        """js日历控件处理 去掉元素的readonly属性 设置value属性直接赋值"""
        js = 'document.getElementById("%s").removeAttribute("readonly");'\
             'document.getElementById("%s").value="%s"' %(calendar,calendar,date)
        self.driver.execute_script(js)
    def is_div_scrollTop(self,divid,n=10000):
        """js处理内嵌div滚动条 向下滚动"""
        js = 'document.getElementById("%s").scrollTop=%s' %(divid,n)
        self.driver.execute_script(js)
    def is_div_scrollLeft(self,divid,n=10000):
        """js处理内嵌div滚动条 向右滚动"""
        js = 'document.getElementById("%s").scrollLeft=%s' %(divid,n)
        self.driver.execute_script(js)
    def getTime(self):
        """获取实时时间"""
        self.now = time.strftime("%Y_%m_%d_%H_%M_%S")
        return self.now
# if __name__ == "__main__":
#     from selenium import webdriver
#     driver = webdriver.Chrome()
#     linken = Base(driver)
#     linken.driver_get()
#     linken.max_window()
#     loc1 = ("id","sux")
#     lk = linken.is_text_to_be_present_in_element(loc1,"xx")
#     print(lk)
#     print(driver.title)
#     linken.driver_quit()



