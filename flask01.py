
from flask import Flask, render_template,request,redirect

import cx_Oracle as oci #pip install cx_oracle

#아이디/ 암호@서버주소:포트번호/SID
conn = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding='utf-8')
cursor = conn.cursor()

app = Flask(__name__) 

@app.route('/')           #페이지를 만드는 부분
def index():
    sql = "SELECT * FROM MEMBER"
    cursor.execute(sql)
    data = cursor.fetchall() #[(),(),()]
    return render_template('list.html', list=data)
   
    for i in data:
       print(i[3])
    
    
    return "index page"

@app.route('/join',methods=['GET'])
def join():
    return render_template('join.html')  #html 템플릿 파일을 가져와서 화면에 뿌려라 
    
@app.route('/join', methods=['POST'])
def join_post():
    a = request.form['id']
    b = request.form['pw']
    c = request.form['name']
    d = request.form['age']
    print("{}:{}:{}:{}".format(a,b,c,d))
    sql = "INSERT INTO MEMBER VALUES(:id,:pw,:na,:ag, SYSDATE)" #sql문 공부하기
    cursor.execute(sql, id=a,pw=b,na=c,ag=d)
    conn.commit() #적용한다는 의미

    #DB에 값을 넣고

    #오라클 DB 접속
    #추가하는 SQL문 작성 => INSERT, SELECT, UPDATE, DELETE
    #SQL문 수행



    return redirect('/') #127.0.0.1:5000/abc
    #127.0.0.1/ 크롬에서 입력한것처럼 동작   


@app.route('/login',methods=['GET'])
def login():
    return render_template('login.html')  #html 템플릿 파일을 가져와서 화면에 뿌려라 

@app.route('/login', methods=['POST'])
def login_post():
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True) # 소스가 바뀌면 재구동 해라