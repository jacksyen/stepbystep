启动，关闭浏览器
===

# python 启动browser
进行web ui的测试首先就要学会启动browser
```python
    # _*_ coding=utf-8 _*_
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    driver.quit
```

# 其他浏览器呢？
其他浏览器，可以自己摸索哦

# 启动其他浏览器
```python
ie= webdriver.Ie
safari=webdriver.Safari
phjs=webdriver.PhantomJS
```

# 关闭driver
