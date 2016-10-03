# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import os

os.environ["SELENIUM_SERVER_JAR"] = "selenium-server-standalone-2.53.1.jar"

driver = webdriver.Safari(quiet=True)
driver.get('https://www.baidu.com')
assert u'百度一下，你就知道' in driver.title
print u"当前URL：", driver.current_url
time.sleep(4)
driver.quit()
