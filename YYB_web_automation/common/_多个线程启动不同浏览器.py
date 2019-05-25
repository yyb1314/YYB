# coding:utf-8
from selenium import webdriver
import time
from tomorrow import threads
'''
如果想用多个浏览器跑同一套测试代码，driver=webdriver.Firefox()这里的driver就不能写死了，可以把浏览器名称参数化。
后续如果想实现多线程同时启动浏览器执行用例，用前面讲的tomorrow模块，设置下线程数套用下就可以了
为了实现多个浏览器的灵活切换，可以把启动浏览器写一个函数，参数用浏览器名称就行了
'''
def startBrowser(name):
    """
    打开浏览器函数，"firefox"、"chrome"、"ie"、"phantomjs"
    """
    try:
        if name == "firefox" or name == "Firefox" or name == "ff":
            print("start browser name :Firefox")
            driver = webdriver.Firefox()
            return driver
        elif name == "chrome" or name == "Chrome" or name == "cc":
            print("start browser name :Chrome")
            driver = webdriver.Chrome()
            return driver
        elif name == "ie" or name == "Ie" or name == "ii":
            print("start browser name :Ie")
            driver = webdriver.Ie()
            return driver
        elif name == "phantomjs" or name == "Phantomjs":
            print("start browser name :phantomjs")
            driver = webdriver.PhantomJS()
            return driver
        else:
            print("Not found this browser,You can use 'firefox', 'chrome', 'ie' or 'phantomjs'")
    except Exception as msg:
        print("启动浏览器出现异常：%s" % str(msg))

@threads(5)
def run_case(name):
    driver = startBrowser(name)
    driver.get("https://www.cnblogs.com/yoyoketang/")
    time.sleep(3)
    print(driver.title)
    driver.quit()

if __name__ == "__main__":
    names = ["chrome"]
    for i in names:
        run_case(i)