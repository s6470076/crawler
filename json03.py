#json3 는 웹에서 가져온 것
import requests
import json
import cx_Oracle as oci

conn = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding='utf-8')
print(conn)
cursor = conn.cursor()

url = "http://ihongss.com/json/exam3.json"
str1= requests.get(url).text
data1 = json.loads(str1) #str -> dict로 타입 변경
#data1 = {ret:[{},{},{}], ret1:[{},{},{}]}
ret1 = data1['ret1'] #[{},{},{},{}]=> [A,B,C,D]
#ret1 = data1['ret1']

for tmp in ret1:#4번 수행
    print(tmp) #{id : "a2001", name : "123", age : "34"}
    sql = """
    INSERT INTO MEMBER(ID,PW,NAME,AGE,JOINDATE)
    VALUES(:ID, 'babo', :NAME, :AGE, SYSDATE)
    """

    cursor.execute(sql, tmp)
    conn.commit()