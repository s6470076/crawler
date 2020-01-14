import requests
import json
import pymongo

conn = pymongo.MongoClient('192.168.99.100', 32766)
db = conn.get_database("db1")#없으면 db1 생성
table = db.get_collection("exam4") #collectiov 생성

url = "http://ihongss.com/json/exam4.json"
str1= requests.get(url).text
data1 = json.loads(str1) #str -> dict로 타입 변경

"""
[{'name': 'AAA', 'species': 'cat', 'foods': {'likes': ['tuna', 'catnip'], 'dislikes': ['ham', 'zucchini']}},
 {'name': 'BBB', 'species': 'dog', 'foods': {'likes': ['bones', 'carrots'], 'dislikes': ['tuna']}}, 
 {'name': 'CCC', 'species': 'cat', 'foods': {'likes': ['mice'], 'dislikes': ['cookies']}}]
"""

print(data1)

for tmp in data1:
    dict1 = dict()
    dict1['name'] = tmp['name']
    dict1['species'] = tmp['species']
    dict1['like'] = tmp['foods']['likes'][0]
    dict1['dislike'] = tmp['foods']['dislikes'][0]
    

    table.insert_one(dict1) #추가하기

conn.close()