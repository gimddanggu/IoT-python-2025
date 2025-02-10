from tkinter import *
import tkinter.font as fnt

root = Tk()
root.geometry('600x400')
root.title('카운트 예제') # 윈도우 창 제목변경

# 이벤트
count = 0 # 계속 증가시킬 수를 담는 변수

def countUp():
    global count # 전역변수 count를 함수 내에서 사용할 거야
    count += 1
    print('카운트 +1')
    label['text'] = f'버튼 클릭: {count:2d}' # 라벨에 표시

def countInit():
    global count
    count = 0
    label['text'] = f'버튼 클릭: 0'

myfont = fnt.Font(family='NanumGothic', size=15)
# 숫자 카운트를 표시할 라벨
label = Label(root, text='버튼 클릭: 0', fg='blue', font=myfont)
# side = LEFT, TOP, RIGHT, BOTTOM
# padding = 안쪽 여백, padx(왼쪽 오른쪽 여백을 줌,), pady(위, 아래 여백)
label.pack(side=TOP, pady = 20)
# 버튼, command 파라미터 - 이벤트 함수를 정의
buttonUp = Button(root, text='카운트', font=myfont, command=countUp) # countUp 함수 마우스 클릭 때마다 실행
buttonUp.pack(side=LEFT, padx=20, pady=20)
buttonInit = Button(root, text='초기화', font=myfont, command=countInit) # countInit 함수 실행
buttonInit.pack(side=LEFT, padx=20, pady=20)
root.mainloop()
