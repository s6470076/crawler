#json10은 mongodb로 자료를 넣는다
import requests
import json
import pymongo

conn = pymongo.MongoClient('192.168.99.100', 32766)
db = conn.get_database("db1")#없으면 db1 생성
table = db.get_collection("exam10") #collectiov 생성

url = "http://ihongss.com/json/exam10.json"
str1 = requests.get(url).text
data1 = json.loads(str1)

"""
 [
 {'id': 'id1', 'name': '가나다1', 'age': 31, 'score': {'math': 50, 'eng': 90, 'kor': 69}}, 
 {'id': 'id2', 'name': '가나다2', 'age': 32, 'score': {'math': 90, 'eng': 68, 'kor': 80}},
 {'id': 'id3', 'name': '가나다3', 'age': 33, 'score': {'math': 70, 'eng': 76, 'kor': 60}},
 {'id': 'id4', 'name': '가나다4', 'age': 34, 'score': {'math': 80, 'eng': 79, 'kor': 50}},
 {'id': 'id5', 'name': '가나다5', 'age': 35, 'score': {'math': 80, 'eng': 78, 'kor': 90}}
 ]
"""


for tmp in data1['data']:
    dict1         = dict()
    dict1['id']   = tmp['id']
    dict1['name'] = tmp['name']
    dict1['age']  = tmp['age']
    dict1['math'] = tmp['score']['math']

    print(data1)
    

    table.insert_one(dict1) #추가하기

conn.close()