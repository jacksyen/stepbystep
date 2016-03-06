# _*_ coding=utf-8 _*_
__author__ = 'patrick'
from selenium import webdriver


def before_all(context):
    context.driver = webdriver.Chrome()

def after_all(context):
    context.driver.quit()
