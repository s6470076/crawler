from selenium import webdriver
import time

options = webdriver.ChromeOptions() #웹 브라우저를 크롬으로 설정하겠다
options.add_argument('headless')  # 창 없이 터미널에서만 보여주겠다

options.add_argument("disable-gpu") # gpu가속을 사용하지 않겠다...  
options.add_argument("lang=ko_KR")  # 한글 사용  
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 
# 로봇이 행위자인지 판별하는 프로그램에 걸리지 않기 위해서 사용

driver = webdriver.Chrome('./chromedriver.exe', options=options)

driver.get("https://finance.naver.com/item/main.nhn?code=035720")

time.sleep(3)
# classname > selector > xpath > full xpath 
a1 = driver.find_element_by_css_selector("#aside > div:nth-child(6)") # <>
a2 = a1.find_element_by_class_name('rank')
a3 = a2.find_elements_by_tag_name("tr") # [<>, <> ...]
# print(a3)

for tmp in a3:
    # a4 = tmp.find_element_by_tag_name("a") # <>
    
    a4 = tmp.find_elements_by_tag_name("a") # [<>]
    if (a4 == []):
        print("공백")
    else:
        print(a4[0].text)
    

# tag = driver.find_element_by_class_name('aside_section cop_list') \
#     .find_elements_by_tag_name("tr")

# for tmp in tag:
#     print(tmp.text.split("\n"))