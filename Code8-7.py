import pymysql
from tkinter import *
from tkinter import messagebox

## 메인 코드부(입력 버튼을 클릭할 때 실행 되는 함수)

def insertData() :
    con, cur = None, None
    data1, data2, data3, data4 = "", "", "", ""
    sql=""

    conn = pymysql.connect(host='127.0.0.1', user='root', password='0000', db='soloDB', charset='utf8')
    cur = conn.cursor()

    # 화면의 4개 엔트리에서 값을 가져옴
    data1 = edt1.get();    data2 = edt2.get();
    data3 = edt3.get();    data4 = edt4.get();

    # 쿼리문을 만들어서 실행
    sql = "INSERT INTO userTable VALUES('" + data1 + "','" + data2 + "','" + data3 + "'," + data4 + ")"
    cur.execute(sql)

    # 데이터를 추가하닌까 commit() 해주기
    conn.commit()
    conn.close()

    messagebox.showinfo('성공', '데이터 입력 성공')

# 조회 버튼을 클릭할 때 데이터를 조회하는 함수
def selectData() :
    strData1, strData2, strData3, strData4  = [], [], [], [] # 리스트 박스에 출력하기 위한 빈 리스트 생성

    conn = pymysql.connect(host='127.0.0.1', user='root', password='0000', db='soloDB', charset='utf8')
    cur = conn.cursor()
    cur.execute("SELECT * FROM userTable")

    # 제목 및 구분하기 위한 줄을 리스트에 추가
    strData1.append("사용자 ID");      strData2.append("사용자 이름")
    strData3.append("사용자 이메일");   strData4.append("사용자 출생연도")
    strData1.append("-----------");    strData2.append("-----------")
    strData3.append("-----------");    strData4.append("-----------")
    
    while (True) :
        row = cur.fetchone()
        if row== None :
            break;
        strData1.append(row[0]);        strData2.append(row[1])
        strData3.append(row[2]);        strData4.append(row[3])

  # 입력된 데이터를 모두 비우는 작업  
    listData1.delete(0,listData1.size() - 1);    listData2.delete(0,listData2.size() - 1)
    listData3.delete(0,listData3.size() - 1);    listData4.delete(0,listData4.size() - 1)

  # 그리고 리스트 추가
    for item1, item2, item3, item4 in zip(strData1, strData2, strData3, strData4 ):
        listData1.insert(END, item1);        listData2.insert(END, item2)
        listData3.insert(END, item3);        listData4.insert(END, item4)
        
    conn.close()    


## 메인 코드부
root = Tk()
root.geometry("600x300")
root.title("완전한 GUI 응용 프로그램")

edtFrame = Frame(root);
edtFrame.pack()
listFrame = Frame(root)
listFrame.pack(side = BOTTOM,fill=BOTH, expand=1)

# 엔트리 데이터 입력 부분 만들기
edt1= Entry(edtFrame, width=10);    edt1.pack(side=LEFT,padx=10,pady=10)
edt2= Entry(edtFrame, width=10);    edt2.pack(side=LEFT,padx=10,pady=10)
edt3= Entry(edtFrame, width=10);    edt3.pack(side=LEFT,padx=10,pady=10)
edt4= Entry(edtFrame, width=10);    edt4.pack(side=LEFT,padx=10,pady=10)

btnInsert = Button(edtFrame, text="입력", command = insertData)
btnInsert.pack(side=LEFT,padx=10,pady=10)

btnSelect = Button(edtFrame, text="조회", command =selectData )
btnSelect.pack(side=LEFT,padx=10,pady=10)

# 리스트 박스 생
listData1 = Listbox(listFrame,bg = 'yellow');
listData1.pack(side=LEFT,fill=BOTH, expand=1)
listData2 = Listbox(listFrame,bg = 'yellow')
listData2.pack(side=LEFT,fill=BOTH, expand=1)
listData3 = Listbox(listFrame,bg = 'yellow')
listData3.pack(side=LEFT,fill=BOTH, expand=1)
listData4 = Listbox(listFrame,bg = 'yellow')
listData4.pack(side=LEFT,fill=BOTH, expand=1)

root.mainloop()
