# -*- coding: utf-8 -*-

from sm import ff, auto_close
from selenium.webdriver.support.ui import Select
import time


@auto_close
def func():
    select = Select(ff.find_element_by_xpath("//select[@name='car']"))
    select.select_by_visible_text("infinity")
    time.sleep(2)
    select.select_by_value("bmw")
    time.sleep(2)
    select.select_by_index("0")
    time.sleep(2)
    # form = ff.find_element_by_name('survey')
    # form.submit()
    submit = ff.find_element_by_id('submit')
    submit.click()
