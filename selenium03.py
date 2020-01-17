#이미지 크롤링
from selenium import webdriver
import urllib.request
import time

#절대경로 가져오기(why? url이미지가 불안정 해서 이미지가 있다가 없다가 해서)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(os.path.join(BASE_DIR,"python"))

options = webdriver.ChromeOptions()

options.add_argument('headless') #화면표시 안 함
options.add_argument("disable-gpu") #옵션
options.add_argument("lang=ko_KR") #한국어
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 

driver = webdriver.Chrome('./chromedriver.exe',options=options) #크롬드라이버를 실행 할 건데, 옵션을 줄어야. 그 옵션은 윗 줄에 내가 선언해 놓은 옵션들이야

url = "http://ihongss.com/home/post?id=p_1579160264639"
driver.get(url) #url을 가져온다
img = driver.find_element_by_css_selector('#image_view_0') #css_selector을 이용해 이미지를 찾아서 들고 온다(), #image_view_0는 아이디를 의미한다
print(img)

file = img.get_attribute("src") #찾은 태그 중에서 src의 값 
urllib.request.urlretrieve(file,"./download/a2.png")

driver.close()