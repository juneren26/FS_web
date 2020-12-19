# coding=utf-8
'''
@Time   :2020/11/25 18:18
@Author :六月
@Email  :juneren26@gmail.com
@File   :chrome_options.py
@IDE    :PyCharm
'''
from selenium import webdriver

class Options:
    def options_conf(self):
        options = webdriver.ChromeOptions()
        # 去掉小黄条
        options.add_experimental_option('excludeSwitches',['enable-automation'])
        # 窗体最大化
        options.add_argument('start-maximized')
        # 去掉密码管理弹窗
        prefs = {}
        prefs['credentials_enable_service'] = False
        prefs['profile.password_manager_enable'] = False
        options.add_experimental_option('prefs',prefs)
        # 加载浏览器本地缓存
        # options.add_argument(r'--user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data')
        # 无头模式
        # options.add_argument('--headless')
        return options

if __name__ == '__main__':
    options = Options.options_conf()
    driver =webdriver.Chrome(options=options)