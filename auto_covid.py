from random import random
from selenium import webdriver
import ssl
import random
import time
from selenium.webdriver.common.action_chains import ActionChains
ssl._create_default_https_context = ssl._create_unverified_context

f = open('id.txt', 'r')
ID = f.read()
f.close()

driver_path ='/Users/jess88tw/webdriver/chromedriver'
driver = webdriver.Chrome(driver_path)
url = 'http://emphm.healthconn.com/#/mgr/login'
driver.get(url)
driver.find_element_by_xpath('/html/body/ngx-app/ngx-page-view/ngx-sample-layout/nb-layout/div/div/div/div/div/nb-layout-column/login/div/form/div/div[2]/input').send_keys(str(ID))
driver.find_element_by_xpath('/html/body/ngx-app/ngx-page-view/ngx-sample-layout/nb-layout/div/div/div/div/div/nb-layout-column/login/div/form/div/button').click()
temp = ['36.4', '36.5', '36.7', '36.9', '36.8', '36.6']

def selectRandom(temp):
  return random.choice(temp)

time.sleep(1)
driver.find_element_by_xpath('/html/body/ngx-app/ngx-page-view/ngx-sample-layout/nb-layout/div/div/div/div/div/nb-layout-column/question2/div[2]/div[1]/div[3]/div/div[2]/input').send_keys(selectRandom(temp))
time.sleep(3)
element_to_hover_over = driver.find_element_by_class_name('ncov-btn_1')
ActionChains(driver).move_to_element(element_to_hover_over).click().perform()
time.sleep(5)
driver.quit()