#bs2.py

from bs4 import BeautifulSoup
import requests



url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cnt&date=20170714"
str = requests.get(url)
#print(str.text)


soup = BeautifulSoup(str.text, 'html.parser')



all_div_tit3 = soup.find_all('div',{"class":"tit3"})
#print(all_div_tit3)
for tmp in all_div_tit3:
    # < a href = "#", id = "aaa">가나다</a>일 경우
    # <span abc="1">가나다</span>
    #print(tmp.find("span").text) #a태그 전부 찾아라 , 가나가 출력 됨

    print(tmp.find("a").attrs)# {'href':'#','id':'aaa'} 딕셔너리**로 출력 됨
    # {'href': '/movie/bi/mi/basic.nhn?code=156477', 'title': '극장판 짱구는 못말려 : 습격!! 외계인 덩덩이'}

    print(tmp.find("a"))# {'href':'#','id':'aaa'} 딕셔너리로 출력 됨
    # <a href="/movie/bi/mi/basic.nhn?code=156477" title="극장판 짱구는 못말려 : 습격!! 외계인 덩덩이">극장판 짱구는 못말려 : 습격!! 외계인 덩덩이</a>










"""
<div class="tit3">
    <a href="/movie/bi/mi/basic.nhn?code=62586" title="다크 나이트">다크 나이트</a>
</div>
"""