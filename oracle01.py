import cx_Oracle as oci


conn = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding='utf-8')
print(conn)

cursor = conn.cursor()

sql = "SELECT * FROM MEMBER"
cursor.execute(sql)
data = cursor.fetchall() #[(),(),()]
print(data)

sql = """
    INSERT INTO MEMBER(ID,PW,NAME,AGE,JOINDATE)
    VALUES(:1, :2, :3, :4, SYSDATE)
    """

arr = ['a1', 'a1', '박소현', 25]
cursor.execute(sql, arr)
conn.commit()

