# py02_gemini_app.py
# tkinter 클래스화

from tkinter import * 
from tkinter.messagebox import * 
from tkinter.scrolledtext import ScrolledText
from tkinter.font import *
import google.generativeai as genai

genai.configure(api_key='AIzaSyAx4QC8gV3ZJ0IV65l1bP-fgPG7SKnhji8') # 신청한 api 키 
model = genai.GenerativeModel('gemini-1.5-flash')


class Window(Tk):
    # 윈도우 창 초기화
    def __init__(self):
        super().__init__() # 부모 객체도 같이 초기화
        self.title('제미나이 챗봇 v2.0')
        self.geometry('730x450')
        self.iconbitmap('chatbot-_2_.ico')
        # 클래스 작업할 땐 self... 유심히
        self.protocol('WM_DELETE_WINDOW', self.onClosing)

        self.initWindow()

    # 닫기 창 눌렀을 때 확인 창 띄우는 함수
    def onClosing(self):
        if askokcancel('종료확인', '종료 하시겠습니까?'):
            self.destroy() # 완전종료

    # 키보드 눌렀을 때 나타나는 함수
    def keypress(self, event):
        if event.char == '\r':
            self.responseMessage()
            self.textMessage.delete('1.0', END)

    # UI 구성요소 초기화(프레임, 버튼, 텍스트, 버튼, 스크롤)
    def initWindow(self):
        self.myfont = Font(family='NanumGothic', size=10)
        self.boldFont = Font(family='NanumGothic', size=10, weight=BOLD)

        self.inputFrame = Frame(self, height=30, width=730, bg='#EFEFEF', padx=10)
        self.inputFrame.pack(side=BOTTOM, fill=BOTH)

        self.textMessage = Text(self.inputFrame, height=1, wrap=WORD, padx=15, font=self.myfont)
        self.textMessage.bind('<Key>', self.keypress) 
        self.textMessage.pack(side=LEFT)

        self.buttonSend = Button(self.inputFrame, text='전송', bg='green', fg='white', padx=20, pady=2, command=self.responseMessage, font=self.myfont)
        self.buttonSend.pack(side=RIGHT)

        self.textResult = ScrolledText(self, wrap=WORD, bg='black', fg='white', font=self.myfont)
        self.textResult.pack(fill=BOTH, expand=True)

        self.textResult.tag_configure('user', font=self.boldFont, foreground='yellow')
        self.textResult.tag_configure('ai', font=self.myfont, foreground='limegreen')
        self.textResult.tag_configure('error', font=self.boldFont, foreground='red')

        self.textMessage.focus_set()
        

    # 전송 버튼 눌렀을 때 호출되는 함수
    def responseMessage(self):
        # showinfo('동작', '이제 api를 호출하면 됩니다.')
        inputText = self.textMessage.get('1.0', END).replace('\n', '').strip()
        print(inputText)

        try:
            if inputText:
                self.textResult.insert(END, '유저: ', BOLD)
                self.textResult.insert(END, f'{inputText}\n\n', 'user')

                ai_response = model.generate_content(inputText)
                response = ai_response.text

                self.textResult.insert(END, '챗봇: ', 'bold')
                self.textResult.insert(END, f'{response}\n', 'ai')

        except Exception as e:
            self.textResult.insert(END, f'Error: {str(e)}\n\n', 'error')
        
        finally:
            self.textResult.see(END)




if __name__ =='__main__':
    print('tkinter 클래스 시작')
    app = Window()
    app.mainloop()

## 궁금한 점
'''
1. 파이썬은 한 줄씩 실행하는 것으로 알고 있는데 mainloop()는 왜 마지막 줄에 있나?
2. __init__이 있는데 initWindow() 함수를 만든 이유?
3. 이벤트 함수 동작 
4. .tag_configure()는 모든 컴포넌트에 존재하는가? 
5. scrolledtext는 왜 inputFrame에 없는가?
6. '1.0', END와 같은 키워드 
'''