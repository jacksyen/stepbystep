# _*_ coding=utf-8 _*_

import os
from selenium import webdriver
import time


__author__ = 'patrick'

driver = webdriver.Chrome()
time.sleep(2)

form_path = 'file:///'+os.path.abspath('form.html')

# by id
driver.find_element_by_id('inputEmail').click()
# by name
driver.find_element_by_name('password').click()
#by tag_name
driver.find_element_by_tag_name('form').get_attribute("class")

#by class name
element = driver.find_element_by_class_name('controls')
driver.execute_script('$(arguments[0]).fadeOut().fadeIn()',element)
time.sleep(2)

#by link text
element = driver.find_element_by_link_text('register')
driver.execute_script('$(arguments[0]).fadeOut().fadeIn()',element)
time.sleep(2)

# by partial link text
element = driver.find_element_by_partial_link_text('reg')
driver.execute_script('$(arguments[0]).fadeOut().fadeIn()',element)
time.sleep(2)

# by css selector
element = driver.find_element_by_css_selector('.controls')
driver.execute_script('$(arguments[0]).fadeOut().fadeIn()',element)
time.sleep(2)

# by xpaht
element = driver.find_element_by_xpath('/html/body/form/div[3]/div/label/input')
driver.execute_script('$(arguments[0]).fadeOut().fadeIn()',element)
time.sleep(2)

driver.quit()
