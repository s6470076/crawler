import csv
import readline
import pandas as pd
import pymongo

conn  = pymongo.MongoClient('192.168.99.100', 32766)
db    = conn.get_database("mini_project") # 있으면 가져오고, 없으면 만들어
table = db.get_collection("korean_chulguk") # 있으면 가져오고, 없으면 만들어

f   = open('./resources/korean_chulguk.csv','r', encoding="euc-kr")

rdr = csv.reader(f)
print(rdr)

column = next(rdr) #[컬럼명 읽기]


for line in rdr:
    dict1 = dict()    
    for idx, val in enumerate(line):
        dict1[column[idx]] = val
        print(line)
          

    table.insert_one(dict1)
conn.close()
