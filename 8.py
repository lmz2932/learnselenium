# -*- coding: utf-8 -*-

from sm import ff, auto_close
from sm import sleep


@auto_close
def func():
    # frames = ff.find_elements_by_tag_name('iframe')
    # ff.switch_to_frame(frames[0])
    # element = ff.find_element_by_name('wd')
    # element.clear()
    # element.send_keys("This is a test")
    # # 切换到顶级frame，然后才可以切换到其他iframe
    # ff.switch_to_default_content()
    # ff.switch_to_frame(frames[-1])
    # element = ff.find_element_by_name('email')
    # element.clear()
    # element.send_keys("Input to sohu")
    ff.switch_to_frame('frame1')
    element = ff.find_element_by_name('wd')
    element.clear()
    element.send_keys("This is a test")
    sleep(2)
    # 切换到顶级frame，然后才可以切换到其他iframe
    ff.switch_to_default_content()
    ff.switch_to_frame('frame2')
    element = ff.find_element_by_name('email')
    element.clear()
    element.send_keys("Input to sohu")
