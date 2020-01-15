#pip install pymongo
import pymongo
import cx_Oracle as oci

conn_o = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding='utf-8')
cursor = conn_o.cursor()

conn = pymongo.MongoClient('192.168.99.100', 32766)
db   = conn.get_database("db1") #없으면 db1 생성
coll = db.get_collection("p20200115") #collection 생성

coll.insert_one({"id":"a","name":"b","age":33})

#SELECT * FROM p20200115
data1  = coll.find({},{"_id":False})
for tmp in data1:
    print(tmp)
    sql = """
    INSERT INTO TABLE1(NO,ID,NAME,AGE)
    VALUES(SEQ_TABLE1_NO.nextval,:id, :name, :age)
    """
    cursor.execute(sql, tmp)
    conn_o.commit()

conn_o.close()#오라클 연결 끊기
conn.close()  #몽고DB연결 끊기

"""

#SELECT * FROM p20200115 WHERE ID="a"
data2  = coll.find({'id':'a'})
for tmp in data2:
    print(tmp)

#SELECT ID, NAME FROM p20200115 WHERE ID = "a"
data3  = coll.find({'id':'a'},{'id':1, 'name':1})
for i in data3:
    print(tmp)

#SELECT * FROM TABLE WHERE age > 10
data4  = coll.find({'age':{'$gt':10}})

#SELECT * FROM TABLE ORDER BY name ASC
data5  = coll.find().sort('name',1) # 1(ASC), -1(DESC)
for tmp in data5:
    print(tmp)

#SELECT * FROM TABLE WHERE age>=10 AND age<=30
data6  = coll.find({"age":{"$gte":10, "$lte":30}})

#SELECT COUNT(*) FROM TABLE
data7  = coll.find().count()
print(data7) #반복문 x, 딕셔너리 아님

#SLELCT * FROM TABLE WHERE ID = 'a' OR NAME = 'b'
data8  = coll.find({'$or':[{"id":'a'},{"name":'b'}]})
"""