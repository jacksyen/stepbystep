# _*_ coding=utf-8 _*_
from selenium import webdriver
import time

__author__ = 'patrick'

driver = webdriver.Chrome
time.sleep(2)

driver.maximize_window()
time.sleep(2)


# set browser size
driver.set_window_size(240,320)
time.sleep(2)

# quit WebDriver
driver.quit()