# coding=utf-8
'''
@Time   :2020/12/8 10:03
@Author :六月
@Email  :juneren26@gmail.com
@File   :keywords.py
@IDE    :PyCharm
'''
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from Chromeoptions.chrome_options import Options


def browser(type_):
    try:
        driver = getattr(webdriver, type_)(options=Options().options_conf())
    except Exception as e:
        print(e)
        driver = webdriver.Chrome()
    return driver


class Webkeys:
    # 定义一个浏览器
    # driver = webdriver.Chrome()
    # 初始化构造函数
    def __init__(self, type_):
        self.driver = browser(type_)
        self.driver.implicitly_wait(10)

    # 访问url
    def open(self, **kwargs):
        self.driver.get(kwargs['txt'])

    # 关闭标签页
    def close(self):
        self.driver.close()

    # 退出浏览器
    def quit(self):
        self.driver.quit()

    # 元素定位
    def locator(self, **kwargs):
        try:
            self.driver.find_element(kwargs['name'], kwargs['value'])
        except Exception as e:
            print(e)
        return self.driver.find_element(kwargs['name'], kwargs['value'])

    # 输入
    def input(self, **kwargs):
        self.locator(**kwargs).send_keys(kwargs['txt'])

    # 点击
    def click(self, **kwargs):
        self.locator(**kwargs).click()

    # 悬停
    def suspend(self, **kwargs):
        el = self.locator(**kwargs)
        action = ActionChains(self.driver)
        action.move_to_element(el).perform()

    # 文本断言校验
    def assert_text(self, **kwargs):
        try:
            assert self.locator(**kwargs).text == kwargs['expect']
            return True
        except:
            return False

    # 强制等待
    def wait(self, **kwargs):
        sleep(kwargs['txt'])

    # 显示等待
    def assert_wait(self,**kwargs):
        try:
            el = WebDriverWait(self.driver,kwargs['txt'],0.5).until(lambda el:self.locator(**kwargs))
            return el
        except:
            return False

    # 关闭标签页在切换句柄
    def switch_close(self):
        handles = self.driver.window_handles
        self.close()
        self.driver.switch_to.window(handles[1])

    # 不关闭标签页切换句柄
    def switch_to(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])

    # 切换旧窗体
    def switch_old(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])

    # 获取元素属性进行断言
    def assert_att(self,**kwargs):
        att = self.locator(**kwargs).get_attribute(kwargs['txt'])
        try:
            assert att ==str(kwargs['expect'])
            return True
        except:
            return False
