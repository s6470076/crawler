from bs4 import BeautifulSoup

with open ('./resources/exam1.html', encoding = "utf-8") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

    #div태그 첫번째 찾기
    first_div = soup.find("div")
    print(first_div)
    
    #div태그 전체 찾기
    all_divs = soup.find_all("div")
    soup.find_all("div",{"class":"first"})  
    #<div class="first">

    #print(all_divs)  
    for tmp in all_divs:
        #print(tmp)
        all_p = tmp.find_all("p")
        for tmp1 in all_p:
            print(tmp1)#태그 전체
            print(tmp1.text)#태그와 태그 사이에 있는 값만 나온다