#json1번은 파일에서 가져온 것
import json
import cx_Oracle as oci

conn = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding='utf-8')
print(conn)
cursor = conn.cursor()

file1 = open('./resources/exam2.json', encoding="")
#str to dict로 변경 => 데이터 타입을 변경한다
data1 = json.load(file1)

#{"ID", "aaa", "PW": "25"}
sql = """
    INSERT INTO MEMBER(ID,PW,NAME,AGE,JOINDATE)
    VALUES(:ID, :PW, :NAME, :AGE, SYSDATE)
    """

arr = ['a1', 'a1', '박소현', 25]
cursor.execute(sql, data1)
conn.commit()

#print(data1)
#print(type(data1))