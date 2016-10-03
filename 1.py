# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 目前支持的driver有Firefox, Chrome, IE和Remote等
driver = webdriver.Firefox(executable_path="./geckodriver")
# 直到页面被加载完（onload被触发）才将控制权返回脚本
driver.get('https://www.baidu.com')
assert u'百度一下，你就知道' in driver.title
print u"当前URL：", driver.current_url

elem = driver.find_element_by_name('wd')
# 清空预填充内容
elem.clear()
# Keys对象表示键盘按键，如F1、ALT等
elem.send_keys(u'48.HTTP基本认证与摘要认证', Keys.RETURN)

try:
    assert u'Mars Loo的博客' in driver.page_source
except Exception as e:
    print e
finally:
    time.sleep(2)
    # quit方法关闭整个浏览器
    driver.quit()
