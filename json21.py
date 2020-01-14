#json21은 mongodb로 자료를 넣는다
import requests
import json
import pymongo

conn = pymongo.MongoClient('192.168.99.100', 32766)
db = conn.get_database("db1")#없으면 db1 생성
table = db.get_collection("exam21") #collectiov 생성

url = "http://ihongss.com/json/exam21.json"
str1 = requests.get(url).text
data1 = json.loads(str1)
 
a = data1['boxOfficeResult']['showRange']

for tmp in data1["boxOfficeResult"]['dailyBoxOfficeList']:#지금은 문자열 상태
    dict1 = dict()#딕셔너리 값이로 변환
    dict1['showRange'] = a
    #dict1['showRange'] = tmp['showRange'] #딕셔너리는 키를 가지고 있기 떄문에 반복문에 안 쓴다.
    dict1['rankOldAndNew'] = tmp['rankOldAndNew']
    dict1['movieNm'] = tmp['movieNm']
    dict1['salesShare'] = tmp['salesShare']
    dict1['salesAcc'] = tmp['salesAcc']
    dict1['scrnCnt'] = tmp['scrnCnt']
    dict1['showCnt'] = tmp['showCnt']
    

    table.insert_one(dict1) #추가하기

conn.close()

print(data1)
