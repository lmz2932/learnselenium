# -*- coding: utf-8 -*-

from sm import ff, auto_close
from selenium.webdriver.support.ui import Select


@auto_close
def func():
    select = Select(ff.find_element_by_xpath("//select[@name='car']"))
    # 获取所有预选项
    print select.all_selected_options
    # 去选所有选项
    select.deselect_all()
    # 获取所有可选项
    print select.options
