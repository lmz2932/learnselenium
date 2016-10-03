# -*- encoding:utf-8 -*-

from selenium import webdriver
import time

ff = webdriver.Firefox()
ff.get('http://selenium-python.readthedocs.io/faq.html')

# 滚动至页面底部
ff.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)
# 保存屏幕截图
ff.save_screenshot('scroll.jpg')
ff.close()
