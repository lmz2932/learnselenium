# -*- coding: utf-8 -*-

from selenium import webdriver
import time


ff = webdriver.Firefox()
ff.get('http://mars:loo@localhost:5000/')
time.sleep(2)
ff.quit()
