import pymysql

# 전역변수 선언부
con, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
row = None

# 메인코드
conn = pymysql.connect(host='127.0.0.1', user='root', password='0000', db='soloDB', charset='utf8')
cur = conn.cursor()

# SELECT문으로 테이블을 조회하고, 조회한 결과는 cur 변수에 저장
cur.execute("SELECT * FROM userTable")

print("사용자ID    사용자이름    이메일        출생연도")
print("----------------------------------------------------")

while (True):
    row = cur.fetchone() # fechone() 함수로 결과를 한 행씩 추출(모든행을 추출)
    if row == None:
        break
    data1 = row[0]
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]
    print("%5s %10s  %15s %d" % (data1, data2, data3, data4))

conn.close()

# conn.commit()이 없는 이유는 UPDATE, DELETE, INSERT 같은 변경이 없기 때문에
