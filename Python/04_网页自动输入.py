# 操作google浏览器,输入数据

from selenium import webdriver

browser = webdriver.Chrome('/Users/xx/Downloads/chromedriver')

browser.get('http://prod.ci.yit.com/job/yit-prod-resolve-job/build?delay=0sec')



/* 登陆Jenkins */
browser.find_element_by_id('j_username').send_keys('xx')
browser.find_element_by_name('j_password').send_keys('xxxx')
browser.find_element_by_id('yui-gen1').click



browser.find_element_by_link_text('Build with Parameters').click

 


from selenium import webdriver

browser = webdriver.Chrome('/Users/xx/Downloads/chromedriver')

browser.get('http://prod.ci.yit.com/job/yit-prod-resolve-job/build?delay=0sec')

browser.find_element_by_id('j_username').send_keys('xx')
browser.find_element_by_name('j_password').send_keys('xxx')
browser.find_element_by_id('yui-gen1-button').click()


browser.find_element_by_path('//*[@id="main-panel"]/form/table/tbody[2]/tr[1]/td[3]/div/input[2]')
