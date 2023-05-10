from tkinter import *

root = Tk()
root.title("버튼 위젯 만들기")
root.geometry("400x300")

botton1 = Button(root, text='버튼1')
botton2 = Button(root, text='버튼2')
botton3 = Button(root, text='버튼3')


# pack() 함수의 옵션 중 padx=픽셀값, pady=픽셀값을 주어 여백 생성
# side = 버튼의 위치, fill은 수평(X)축으로 전체 너비를 채우도록 설정하는 옵 
botton1.pack(side=TOP, fill=X, padx=10, pady=10)
botton2.pack(side=TOP, fill=X, padx=10, pady=10)
botton3.pack(side=TOP, fill=X, padx=10, pady=10)

root.mainloop()
