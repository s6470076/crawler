#json2 는 웹에서 가져온 것
import requests
import json
import cx_Oracle as oci

conn = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding='utf-8')
print(conn)
cursor = conn.cursor()

"""
{
"ret":{"id":"a386","name":"123","age":34, "pw" : "abc"},
"ret1":{"id":"a383","name":"123","age":36, "pw' : "fds"}
}
"""
url = "http://ihongss.com/json/exam2.json"
str1= requests.get(url).text
data1 = json.loads(str1) #str -> dict로 타입 변경
#ret = data1['ret']# 딕셔너리에 있는 키("ret")의 
                   #값{"id":"a386","name":"123","age":34, "pw" : "abc"}을 불러온다
ret1 = data1['ret1']
sql = """
    INSERT INTO MEMBER(ID,PW,NAME,AGE,JOINDATE)
    VALUES(:ID, '1646', :NAME, :AGE, SYSDATE)
    """

cursor.execute(sql, ret1)
conn.commit()


