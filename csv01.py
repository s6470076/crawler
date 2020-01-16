import csv
import pymongo

#방법1 (데이터 프레임 사용)
conn = pymongo.MongoClient('192.168.99.100', 32766)
db   = conn.get_database("db1") 
coll = db.get_collection("exam1")

f   = open('./resources/exam1.csv','r', encoding="utf-8")
print(f)
rdr = csv.reader(f)
print(type(rdr))
next(rdr, None) # 컬럼 skip
# print(next(rdr, None) )

for line in rdr:
    print(type(line))
    print(line)
#     dict1 = dict()
#     dict1[line[0]] = line
#     coll.insert_one(dict1)

# conn.close()