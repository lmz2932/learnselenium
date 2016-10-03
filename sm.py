# -*- encoding: utf-8 -*-
from selenium import webdriver
from time import sleep

ff = webdriver.Firefox(executable_path="./geckodriver")
ff.get('http://localhost:5000/')
# 6.py中拖放示例使用这个地址
# ff.get('http://html5demos.com/drag')


def auto_close(func):
    try:
        func()
    except Exception as e:
        print "Exception occurs:", e
    finally:
        sleep(2)
        ff.quit()
