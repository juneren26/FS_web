# coding=utf-8
'''
@Time   :2020/11/20 16:35
@Author :六月
@Email  :juneren26@gmail.com
@File   :login_demo.py
@IDE    :PyCharm
'''
# from selenium import webdriver


from Chromeoptions.chrome_options import Options
from FSkeys.keywords import Webkeys
# # 设置浏览器
# driver = webdriver.Chrome(options=Options().options_conf())
# driver.maximize_window()
# driver.implicitly_wait(5)
# # 登陆账号
# driver.get('https://tx.fs.com/cn/index.php?main_page=login')
# driver.find_element_by_id('email_address_login').send_keys('scot.ren@feisu.com')
# driver.find_element_by_id('password_login').send_keys('renzhao95626')
# driver.find_element_by_id('user_login').click()
# # 鼠标悬停
# el = driver.find_element_by_link_text('我的账户')
# action = ActionChains(driver)
# action.move_to_element(el).perform()
# # 校验账号是否登陆成功
# driver.find_element_by_link_text('我的账户').click()
# el = driver.find_element_by_xpath('//div[contains(text(),"FS186002724")]').text
# print(el)
# account = 'FS186002724'
# assert account in el, '断言失败'

driver = Webkeys('Chrome')
driver.open('https://tx.fs.com/cn/index.php?main_page=login')
driver.input('id','email_address_login','scot.ren@feisu.com')
driver.input('id','password_login','renzhao95626')
driver.click('id','user_login')
driver.wait(3)
driver.suspend('xpath','/html/body/div[1]/div/div[5]/div/a')
driver.wait(3)
driver.click('xpath','/html/body/div[1]/div/div[5]/div/div[2]/ul/li[1]/a')
driver.wait(1)
driver.assert_text('FS186002724','xpath','//div[contains(text(),"FS186002724")]')
