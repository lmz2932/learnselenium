# -*- coding: utf-8 -*-

from sm import ff, auto_close
jquery_url = "http://upcdn.b0.upaiyun.com/libs/jquery/jquery-2.0.2.min.js"


@auto_close
def func():
    ff.set_script_timeout(30)
    with open("load_jquery.js") as f:
        load_jquery_js = f.read()

    with open("drag_and_drop.js") as f:
        drag_and_drop_js = f.read()

    ff.execute_async_script(load_jquery_js, jquery_url)

    ff.execute_script(drag_and_drop_js +
                      "$('#one').simulateDragDrop({ dropTarget: '#bin'});")
