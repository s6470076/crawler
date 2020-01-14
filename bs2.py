from bs4 import BeautifulSoup
import requests

"""
<div class="tit3">
    <a href="/movie/bi/mi/basic.nhn?code=62586" title="다크 나이트">다크 나이트</a>
</div>
"""

url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cnt&date=20170714"
str = requests.get(url)
print(str.text)

soup = BeautifulSoup(str.text, 'html.parser')

all_div_tit3 = soup.find_all('div',{"class":"tit3"})
print(all_div_tit3)
for tmp in all_div_tit3:
    print(tmp.find("a").text) #a태그 전부 찾아라
    print(tmp.text)#태그와 태그 사이