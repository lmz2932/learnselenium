# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class BaiduSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="./geckodriver")

    def test_search_in_baidu(self):
        driver = self.driver
        driver.get("http://www.baidu.com")
        self.assertIn(u'百度一下，你就知道', driver.title)
        elem = driver.find_element_by_name("wd")
        elem.send_keys(u"47.HTTP代理（转发代理&反向代理）与重定向")
        elem.send_keys(Keys.RETURN)
        time.sleep(2)
        self.assertIn(u"Mars Loo的博客", driver.page_source)

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
