# -*- coding: utf-8 -*-

from sm import ff, auto_close
import time


@auto_close
def func():
    # 采用xpath获取第一个select元素
    element = ff.find_element_by_xpath("//select[@name='car']")
    # 获取所有选项，打印选项值并点击
    all_options = element.find_elements_by_tag_name("option")
    for option in all_options:
        time.sleep(1)
        print "Value is: %s" % option.get_attribute("value")
        option.click()
