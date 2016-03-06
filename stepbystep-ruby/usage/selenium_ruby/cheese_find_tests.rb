require 'rubygems'
require 'selenium-webdriver'
require 'test/unit'

class CheeseFindTests <Test::Unit::TestCase
  def test_find_some_cheese
    driver = Selenium::WebDriver.for(:firefox)
    driver.get("www.baidu.com")
    driver.find_element(:id,"q").sendKeys("abcde")
    driver.find_element(:id,"kw").sendKeys("abcs")
    driver.find_element(:id,"submit").submit()
    driver.quit
  end
end