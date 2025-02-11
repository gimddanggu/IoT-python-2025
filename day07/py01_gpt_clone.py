# py01._gpt_clone.py

from tkinter import * # tkinter 모듈에 있는 모든 클래스, 함수, 변수등을 다 쓰겠다.
from tkinter.messagebox import * # 모듈 밑에 있는 모듈을 위의 명령어(3번)로 가져올 수 없음
from tkinter.scrolledtext import ScrolledText
from tkinter.font import *
# 제미나이를 위한 모듈
import google.generativeai as genai

# 6. 제미나이 api용 구성
genai.configure(api_key='AIzaSyAx4QC8gV3ZJ0IV65l1bP-fgPG7SKnhji8') # 신청한 api 키 
model = genai.GenerativeModel('gemini-1.5-flash')



# 4. 전송 버튼 이벤트 추가, 제미나이 실행 포함
def responseMessage():
    # showinfo('실행', 'api를 실행합니다')
    inputText = textMessage.get('1.0', END).replace('\n', '').strip()
    print(inputText)
    

    if inputText:
        try:
            # 9. 유저와 챗봇 응답 ui 개선 및 태그 추가
            textResult.insert(END, '유저: ', BOLD)
            textResult.insert(END, f'{inputText}\n\n', 'user') # user' 텍스트 아규먼트

            ai_response = model.generate_content(inputText)
            response = ai_response.text

            textResult.insert(END, '챗봇: ', 'bold')
            textResult.insert(END, f'{response}\n\n', 'ai') # ai 텍스트 태그
            
        except Exception as e:
            textResult.insert(END, f'Error: {str(e)}\n\n', 'error')
        
        finally:
            textResult.see(END) # 마지막 위치로 스크롤 다운

    # showinfo('결과', inputText) # 다이얼로그, 모달창

# 8. textMessage위젯에서 엔터를 치면 전송버튼이 클릭
def keypress(event):
    # print(textMessage.get())
    # print(repr(event.char)) # repr을 안 쓰면 \r, \x08 표시 안 됨
    # \r(캐리지 리턴), \n(뉴라인) 혼용해서 사용 \r\n, \n, \r 세 가지 경우 있음 
    # CRLF는 \r 사용

    if event.char == '\r':
        responseMessage()
        textMessage.delete('1.0', END)
# 12. 종료시 이벤트처리 함수
def onClosing():
    if askokcancel('종료확인', '종료 하시겠습니까?'):
        root.destroy() # 완전종료

# 1. 메인윈도우 생성, 초기설정
root = Tk()
root.title('제미나이 쳇봇')
root.geometry('730x450')

# 13. 아이콘 변경
# pyinstaller로 설치할 땐 해당폴더에 복사하고 
# ./image/ 경로는 삭제
root.iconbitmap('./image/chatbot-_2_.ico') 

# 7. 전체에서 사용할 폰트 지정 -> 나눔고딕
myfont = Font(family='NanumGothic', size=10)
boldFont = Font(family='NanumGothic', size=10, weight=BOLD)

# 2. UI 화면 구성
# 프레임을 넣을 때는 항상 색을 넣을 것!
inputFrame = Frame(root, height=30, width=730, bg='#EFEFEF', padx=10)
inputFrame.pack(side=BOTTOM, fill=BOTH)

# 3. inputFrame에 들어갈 Entry와 Buttom 구성
# wrap: 자동 줄 바꿈
textMessage = Text(inputFrame, height=1, wrap=WORD, padx=15, font=myfont)
# 8. 입력창에서 엔터를 치면 keypress 이벤트 처리 함수 발생
textMessage.bind('<Key>', keypress) 
textMessage.pack(side=LEFT)

buttonSend = Button(inputFrame, text='전송', bg='green', fg='white', padx=20, pady=2, command=responseMessage, font=myfont)
buttonSend.pack(side=RIGHT)

# 5. api 호출 결과 메시지 출력될 텍스트 위젯 추가 + 스크롤 기능
textResult = ScrolledText(root, wrap=WORD, bg='black', fg='white', font=myfont)
textResult.pack(fill=BOTH, expand=True)

# 11. 스크롤 텍스트에 나올 메시지 디자인
textResult.tag_configure('user', font=boldFont, foreground='yellow')
textResult.tag_configure('ai', font=myfont, foreground='limegreen')
textResult.tag_configure('error', font=boldFont, foreground='red')

# 10. 실행 후 바로 입력창에 포커스가 가도록
textMessage.focus_set()

# 12. 종료버튼(x)를 누르면 종료메시지 확인 후 종료
root.protocol('WM_DELETE_WINDOW', onClosing)
# inputFrame()
# 종료시까지 계속 실행
root.mainloop() 