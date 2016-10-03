# -*- coding: utf-8 -*-

from sm import ff, auto_close


@auto_close
def func():
    # 切换到当前弹出框并返回Alert对象
    alert = ff.switch_to_alert()
    # 获取弹出框的文本内容
    print "Alert text:", alert.text
    # 点击弹出框的确定按钮
    # alert.accept()
    # 点击弹出框的取消按钮
    # alert.dismiss()
    # 如果是prompt类型的弹出框，向其中输入内容
    alert.send_keys("This is my choice")
    # 然后点击prompt框的确定按钮
    alert.accept()
