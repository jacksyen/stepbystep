# _*_ coding=utf-8 _*_
from selenium import webdriver
import time

__author__ = 'patrick'

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
time.sleep(2)
driver.quit
print 'browser is closed'

ie= webdriver.Ie
safari=webdriver.Safari
phjs=webdriver.PhantomJS