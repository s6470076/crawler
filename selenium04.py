#웹사이트에서 이미지 여러개 들고오기

from selenium import webdriver
import urllib.request
import time
import os
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
#options.add_argument('headless') #화면표시 안 함
options.add_argument("disable-gpu") #옵션
options.add_argument("lang=ko_KR") #한국어
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 

driver = webdriver.Chrome('./chromedriver.exe',options=options) #크롬드라이버를 실행 할 건데, 옵션을 줄거야. 그 옵션은 윗 줄에 내가 선언해 놓은 옵션들이야
driver.get('http://naver.com')

driver.find_element_by_xpath('//*[@id="query"]').send_keys('사과')
driver.find_element_by_xpath('//*[@id="query"]').send_keys(Keys.ENTER)

driver.find_element_by_xpath('//*[@id="lnb"]/div/div[1]/ul/li[2]/a/span').click()


link = []  
for i in range(1, 5, 1): 
    try:
 
        img = driver.find_element_by_xpath('//*[@id="_sau_imageTab"]/div[1]/div[2]/div['+ str(i) + ']/a[1]/img') 
        print('1')
    except:
        img = driver.find_element_by_xpath('//*[@id="_sau_imageTab"]/div[2]/div[2]/div['+ str(i) + ']/a[1]/img')   
        print('2')    
    link.append(img.get_attribute('src'))


for idx, tmp in enumerate(link):
    urllib.request.urlretrieve(tmp,"./download/n"+str(idx)+".jpg")
