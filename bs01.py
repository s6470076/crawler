from bs4 import BeautifulSoup
#뷰티플수프는 복합적인 HTML 문서를 파이썬 객체로 구성된 복합적인 문서로 변환한다
#HTML과 XML 파일로부터 데이터를 뽑아내기 위한 파이썬 라이브러리
with open ('./crawler/resources/exam1.html', encoding = "utf-8") as fp:
    soup = BeautifulSoup(fp, 'html.parser') #parser => 데이터를 조립해 원하는 데이터를 빼내는 프로그램을 하는것

    #div태그 첫번째 찾기
    first_div = soup.find("div")
    #print(first_div)
    
    #div태그 전체 찾기
    all_divs = soup.find_all("div")
    soup.find_all("div",{"class":"first"})  
    #<div class="first">
    #print(all_divs)  
    for tmp in all_divs:
        print(tmp)
        all_p = tmp.find_all("p")
        for tmp1 in all_p:
            #print(tmp1)#태그 전체 -> <p>a</p> /n <p>b</p>
            print(tmp1.text)#태그와 태그 사이에 있는 값만 나온다 a b
            