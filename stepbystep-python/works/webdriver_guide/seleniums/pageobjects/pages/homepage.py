# _*_ coding=utf-8 _*_
__author__ = 'patrick'
from works.webdriver_guide.seleniums.pageobjects.pages.basepage import BasePage
from works.webdriver_guide.seleniums.pageobjects.pages.basepage import InvalidPageException


class HomePage(BasePage):

    _home_page_slideshow_locator = 'slideshow-container'

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)

    def _validate_page(self, driver):
        try:
            driver.\
                find_element_by_class_name(self._home_page_slideshow_locator)
        except:
            raise InvalidPageException("Home Page not loaded")
