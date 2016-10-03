# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome import service
import time

webdriver_service = service.Service('./operadriver')
webdriver_service.start()
driver = webdriver.Remote(webdriver_service.service_url,
                          webdriver.DesiredCapabilities.OPERA)

driver.get('https://www.baidu.com')
assert u'百度一下，你就知道' in driver.title
print u"当前URL：", driver.current_url
time.sleep(4)

# Opera的退出会报错：
# Exception RuntimeError: RuntimeError('sys.meta_path must
# be a list of import hooks',) in <bound method Service.__del__ of
# <selenium.webdriver.chrome.service.Service object at 0x10ef069d0>> ignored
# 影响是会有operadriver进程残留，需要手动清除
driver.close()
