import tkinter as tk

def event_info(event):
    print(*dir(event), sep=' ')  # event 객체에 어떤 속성이 있는지 출력

root = tk.Tk()
root.bind("<Button-1>", event_info)  # 마우스 왼쪽 버튼 클릭 시 실행
root.mainloop()

