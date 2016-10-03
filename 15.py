# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="./chromedriver")
driver.get('https://www.baidu.com')
assert u'百度一下，你就知道' in driver.title
print u"当前URL：", driver.current_url

elem = driver.find_element_by_name('wd')
elem.clear()
elem.send_keys(u'36.在Ubuntu上打造方便好用的Python开发环境', Keys.RETURN)

try:
    assert u'Mars Loo的博客' in driver.page_source
except Exception as e:
    print e
finally:
    time.sleep(2)
    driver.close()
