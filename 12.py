# -*- coding: utf-8 -*-

from sm import ff, auto_close


@auto_close
def func():
    ff.add_cookie({'name': 'username', 'value': 'marsloo'})
    ff.get('http://localhost:5000/')
    # 获取当前域的cookies
    print ff.get_cookies()
