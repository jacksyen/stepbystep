# _*_ coding=utf-8 _*_
from selenium import webdriver
import time

__author__ = 'patrick'

driver = webdriver.Chrome
time.sleep(2)

driver.get("http://www.baidu.com")
print "web page title is %s" % {driver.title}
print "current page url is %s" % {driver.current_url}
print "current window handler is %s" %{driver.current_window_handle}

time.sleep(1)
driver.quit()