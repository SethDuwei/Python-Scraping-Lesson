from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://my.duanshu.com/login")
element = browser.find_element_by_xpath('//span[@class="register"]')
element.click()
