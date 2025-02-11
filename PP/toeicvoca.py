from tkinter import *
from tkinter.messagebox import * 
from tkinter.font import *
import pandas as pd


class MainWindow(Tk):
    VERSION = 0.1
    
    def __init__(self):
        super().__init__()
        self.title(f'토익단어장 v.{self.VERSION}')
        self.geometry('730x450')
        self.iconbitmap('./image/word.ico')
        self.protocol('WM_DELETE_WINDOW', self.onClosing)

        self.initComponent()

    def onClosing(self):
        if askokcancel('종료확인', '종료 하시겠습니까?'):
            self.destroy()
        

    def addWord(self):
        idx = len(self.word_df)
        self.word_df.loc[idx + 1] = [self.word.get(), self.meaning.get()]
        print([self.word.get(), self.meaning.get()])
        print(self.word_df)

    def saveFile(self):
        self.word_df.to_excel('test_word.xlsx')
        print('파일저장 성공!')

    def initComponent(self):
        # 일단 단어 추가 기능만
        self.addWordButton = Button(self, text='단어추가', command=self.addWord)
        self.saveButton = Button(self, text='단어저장', command=self.saveFile)
        # self.searchWordButton = Button(self, text='단어검색')
        # self.testWordButton = Button(self, text='단어테스트')
        self.addWordButton.grid(column=3,rowspan=2)
        # self.searchWordButton.pack()
        # self.testWordButton.pack()
        self.word_l = Label(self, text='단어')
        self.meaning_l = Label(self, text='뜻')
        self.word_l.grid(column=0, row=0)
        self.meaning_l.grid(column=0, row=1)
        self.word = Entry(self)
        self.meaning = Entry(self)
        self.word.grid(column=1, row=0)
        self.meaning.grid(column=1, row=1)
        self.saveButton.grid(columnspan=2, row=2)

        # 데이터 담을 데이터 프레임 생성
        self.word_df = pd.DataFrame(columns=['단어', '뜻'])

    



        # 단어추가하는 로직 
        # 엑셀파일 열기
        # 버튼을 누를 때, 엔터를 누를 때 이벤트 발생
        # 단어 추가 종료를 누르면 파일 저장

        # _tkinter.TclError: cannot use geometry manager grid inside . which already has slaves managed by pack
        # PS C:\dev\python\IoT-python-2025>
        
        # 2025.02.12 단어추가 -> 엑셀파일로 저장 기능 구현



if __name__ == '__main__':
    print('토익단어장 실행')
    app = MainWindow()
    app.mainloop()