# -*- coding: utf-8 -*-

from sm import ff, auto_close
from sm import sleep


@auto_close
def func():
    a = ff.find_element_by_tag_name('a')
    a.click()
    print "Go back"
    sleep(2)
    ff.back()
    print "Go forward"
    sleep(2)
    ff.forward()
