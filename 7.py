# -*- encoding:utf-8 -*-

from sm import ff, auto_close, sleep


@auto_close
def func():
    a = ff.find_element_by_tag_name("a")
    # 保存原始窗口,window_handlers是目前wd打开的所有窗口的句柄列表
    prev = ff.window_handles[-1]
    # 点击超链接(targe="_blank")后,浏览器新窗口被激活
    a.click()
    # 保存新窗口
    new = ff.window_handles[-1]
    # 切换到原始窗口
    sleep(2)
    ff.switch_to_window(prev)
    print "Switch to prev success"
    sleep(2)
    # 切换到新窗口
    ff.switch_to_window(new)
    print "Switch to new success"
