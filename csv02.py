import csv
import readline
import pandas as pd
import pymongo

#csv는 구분자 , \t
df = pd.read_csv('./resources/exam1.csv', delimiter=",")
#print(df)

df = df.dropna() #NaN제거 : 결측치 제거
#print(df)

list1 = df.values.tolist() #DF => list 변경
#print(list1)
dict1 = df.to_dict() #DF => dict 변경
#print(dict1)



#몽고디비에 파일 집어 넣기 과제임

column = (list(df.columns)) # 컬렴명 읽기

## 몽고 접속
conn = pymongo.MongoClient('192.168.99.100', 32766)
db = conn.get_database("db2")
coll = db.get_collection("csv02") 

for line in list1:
    res = dict()
    for idx, val in enumerate(line):
        res[column[idx]] = val
    coll.insert_one(res)
conn.close()
