# 프레임, 엔트리, 리스트 박스 표현하기

from tkinter import *

root = Tk()
root.title("화면 구역 표현")
root.geometry("400x300")

# 2개의 프레임을 생성
upFrame = Frame(root)
upFrame.pack()
downFrame = Frame(root)
downFrame.pack()

# 엔트리 나타내기
editBox = Entry(upFrame, width = 10)
editBox.pack(padx = 20, pady = 20)

# 리스트 박스 나타내기
listbox = Listbox(downFrame, bg = 'yellow')
listbox.pack()

# 리스트박스에 데이터 입력하기
# END는 데이터를 제일 위에 첨부하라는 의미
listbox.insert(END, '하나')
listbox.insert(END, '둘')
listbox.insert(END, '셋')

root.mainloop()
