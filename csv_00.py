import csv
import readline
import pandas as pd
import pymongo

#http://ihongss.com/csv/exam1.csv

# conn = pymongo.MongoClient('192.168.99.100', 32766)
# db = conn.get_database("csv_exam") # 있으면 가져오고, 없으면 만들어
# table = db.get_collection("exam01") # 있으면 가져오고, 없으면 만들어
# 선언까지만 하고 데이터삽입을 안하면 생성 X

## 방법1
df = pd.read_csv('./resources/exam1.csv')
# print(df)
dict1 = df.to_dict()
# print(dict1)

dict2 = dict()
for key, value in dict1.items():
    print(key,value[0])
    dict2[key] = value[0]
    print(dict2)

"""
{'manager_name': 
    {0: 'Arjun Kumar', 
     1: 'Kabir Vish', 
     2: 'Arjun Kumar', 
     3: 'Arjun Kumar', 
     4: 'Rohit Srivastav', 
     5: 'Kabir Vish', 
     6: 'Rohit Srivastav', 
     7: 'Rohit Srivastav', 
     8: 'Kabir Vish'}, 
'client_name': {0: 'Rehan Nigam', 1: 'Abhinav Neel', 2: 'Sam Mehta', 3: 'Ira Pawan', 4: 'Vihaan Sahni', 5: 'Daivik Saxena', 6: 'Lera Uddin', 7: 'Aaran Puri', 8: nan}, 'client_gender': {0: 'male', 1: 'male', 2: 'male', 3: 'female', 4: 'male', 5: 'male', 6: 'female', 7: 'male', 8: 'male'}, 'client_age': {0: 30, 1: 28, 2: 27, 3: 40, 4: 38, 5: 45, 6: 20, 7: 34, 8: 50}, 'response_time': {0: 4.0, 1: 12.0, 2: 3.0, 3: 2.5, 4: 6.0, 5: 16.0, 6: 8.0, 7: 7.5, 8: 20.0},
'statisfaction_level': {0: 0.5, 1: 0.1, 2: 0.7, 3: 0.6, 4: 0.5, 5: 0.2, 6: 0.4, 7: 0.3, 8: 0.1}}
"""


# f = open('./resources/exam1.csv', 'r', encoding="utf-8")

## 방법2
# rdr = csv.reader(f)
# # print(rdr)

# column = next(rdr) #[컬럼명 읽기]
# print(column)
# # # [manager_name,client_name,client_gender,client_age,response_time,statisfaction_level]

# # # [a,b,c,d,e,f] => 0,a 1,b 2,c 3,d
# for line in rdr:
#     print("======================")
#     print(line)
#     dict1 = dict()    
#     # ['Arjun Kumar', 'Rehan Nigam', 'male', '30', '4', '0.5']
#     for idx, val in enumerate(line): #[1,2,3,4,5,6] # enumerate - index, val
#         # 0, 'Arjun Kumar' /
#         #dict1["manager_name"] = 'Arjun Kumar'
#         dict1[column[idx]] = val
#     # print(dict1)
#     table.insert_one(dict1)
#     print("insert success")

# conn.close()