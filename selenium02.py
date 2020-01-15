#html에 등록 되지 못하는 실시간 자료를 가져올 때
from selenium import webdriver
import time
options = webdriver.ChromeOptions()
options.add_argument('headless')

options.add_argument("disable-gpu")   
options.add_argument("lang=ko_KR")    
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 

driver = webdriver.Chrome('./chromedriver.exe', 
    options=options)

driver.get("https://datalab.naver.com/shoppingInsight/sCategory.naver")

time.sleep(3)
tag = driver.find_element_by_class_name('rank_top1000_list') \
    .find_elements_by_tag_name("li")

for tmp in tag:
    print(tmp.text.split("\n"))
