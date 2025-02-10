# py05_tkinter_widget.py
# Tkinter 위젯 학습용

from tkinter import *
from tkinter.messagebox import *

def buttonClick():
    showinfo('위젯', '버튼을 클릭했습니다!') # 다이얼로그(메시지) 박스

root = Tk()
root.title('위젯 예제')
img = PhotoImage(file='./day06/kitty.png')
label = Label(root, image=img)
label.pack()
# 버튼 위젯
button = Button(root, text='클릭', command=buttonClick)
button.pack()
# 엔트리 위젯 - 사용자 입력
entry = Entry(root)
entry.pack()
# 라디오버튼
Label(root, text='가장 선호하는 프로그래밍 언어 선택').pack()

choice = IntVar()
Radiobutton(root, text='C', value=0, variable=choice).pack()
Radiobutton(root, text='C#', value=1, variable=choice).pack()
Radiobutton(root, text='Python', value=2, variable=choice).pack()
Radiobutton(root, text='Java', value=3, variable=choice).pack()

# 체크박스
Label(root, text='좋아하는 과일을 모두 선택').pack()

orange = IntVar()
banana = IntVar()
mango = IntVar()

Checkbutton(root, text='오렌지', variable=orange).pack(anchor=W)
Checkbutton(root, text='바나나', variable=banana).pack(anchor=W)
Checkbutton(root, text='사과', variable=mango).pack(anchor=W)

# 리스트박스위젯
lstBx = Listbox(root, height = 4)
lstBx.pack()
lstBx.insert(END, 'Pyton')
lstBx.insert(END, 'Java')
lstBx.insert(END, 'Ruby')
lstBx.insert(END, 'PHP')

# 컨테이너 위젯 중(프레임)
frame = Frame(root, width=600, height=40, bg='gray')
frame.pack()
# 프레임에 들어갈 위젯
button2 = Button(frame, text='버튼2', width=80)
button2.pack(side=LEFT)
button3 = Button(frame, text='버튼3', width=80)
button3.pack(side=LEFT)
button4 = Button(frame, text='버튼4', width=80)
button4.pack(side=LEFT)
root.mainloop()