#<로그인 이후 정보를 가져올 때 (다음 카페에서 정보를 가져오는 경우)
from selenium import webdriver
from bs4 import BeautifulSoup
import time


options = webdriver.ChromeOptions()

options.add_argument('window-size=1920x1080')

driver = webdriver.Chrome('./chromedriver.exe', chrome_options=options)

driver.get("http://ihongss.com/webboard")

driver.execute_script("document.getElementsByName('email')[0].value='20191216'")
#driver.find_element_by_name("email").send_keys('20191216')
driver.find_element_by_name("pw").send_keys('20191216')
driver.find_element_by_css_selector('#form1 > div:nth-child(4) > input').click()


#selector
#form1 > div:nth-child(4) > input

#xpath
#//*[@id="form1"]/div[3]/input

#스크랩이 3초 후에 뜬다
time.sleep(3)
driver.execute_script("alert('hello')")

'''
driver.get("http://daum.net")#로그인 이후의 페이지
html = driver.page_source
soup = BeautifulSoup(html, 'html-parser')
'''