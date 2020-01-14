from bs4 import BeautifulSoup
import requests

"""
<div class="txtBox">
    <h4>해운대해수욕장</h4>
    <p>부산광역시 해운대구 해운대해변로 264</p>
</div>
"""

url = "https://bto.or.kr/kor/Main.do"
str = requests.get(url)
#print(str.text)

soup = BeautifulSoup(str.text, 'html.parser')

all_div_want = soup.find_all('ul',{"id":"bful"})
#print(all_div_want)
for tmp in all_div_want:
    # < a href = "#", id = "aaa">가나다</a>일 경우
    #print(tmp.find("h").text) #a태그 전부 찾아라 , 가나가 출력 됨
    #print(tmp.find("h").attrs)# {'href':'#','id':'aaa'} 딕셔너리로 출력 됨
    print(tmp.text)