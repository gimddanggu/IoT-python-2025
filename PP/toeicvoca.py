from tkinter import *
from tkinter.messagebox import * 
from tkinter.font import *
import pandas as pd
import os


class MainWindow(Tk):
    VERSION = 0.1
    
    def __init__(self):
        super().__init__()
        self.title(f'토익단어장 v.{self.VERSION}')
        self.geometry('430x450')
        self.iconbitmap('./image/word.ico')
        self.protocol('WM_DELETE_WINDOW', self.onClosing)

        self.word_df = pd.DataFrame(columns=['단어', '뜻'])


        self.initComponent()

    def onClosing(self):
        if askokcancel('종료확인', '종료 하시겠습니까?'):
            self.destroy()
        

    def addWordEvent(self, event):
        # self.word_df = pd.read_excel('./word.xlsx')
        idx = len(self.word_df)
        self.word_df.loc[idx + 1] = [self.word.get(), self.meaning.get()]
        print([self.word.get(), self.meaning.get()])
        print(self.word_df)

    def saveFile(self):
        self.word_file = pd.read_excel('./word.xlsx', index_col=0)
        new_word = pd.concat([self.word_file, self.word_df])
        new_word.to_excel('word.xlsx')
        print('파일저장 성공!')


    def loadFile(self):
        pass
    def initComponent(self):
        self.appTittle = Label(self, text='TOEIC 단어장')
        self.addWordButton = Button(self, text='단어추가', command=self.new_window)
        self.testWordButton = Button(self, text='단어 테스트', command=self.testWord)
        self.appTittle.pack()
        self.addWordButton.pack()
        self.testWordButton.pack()
    def testWord(self):
        pass

    def new_window(self):
        # 단어 입력 후 엔터로 저장 단어 저장 버튼 누르면 이전 윈도우로 돌아감
        # 창 열리면 자동으로 단어장 준비 완료됨
        if os.path.exists('./word.xlsx'):
            # 파일이 있는지만 확인하자 불러오고 저장은 저장단계에서
            # self.word_file = pd.read_excel('./word.xlsx')
            print('단어장 불러오기 성공')
        else:
            print('단어장을 새로 생성합니다.')
            # self.word_df = pd.DataFrame(columns=['단어', '뜻'])
            self.word_df.to_excel('./word.xlsx')
        # 단어 뜻을 입력하고 엔터를 누르면 단어 추가
        # 단어 저장 누르면 엑셀파일 저장하고 이전 윈도우로 돌아감
        self.nw = Toplevel(self)
        self.nw.title('단어추가')
        self.nw.geometry('180x100')
        self.word_l = Label(self.nw, text='단어')
        self.meaning_l = Label(self.nw, text='뜻')
        self.word = Entry(self.nw)
        self.meaning = Entry(self.nw)
        self.saveButton = Button(self.nw, text='단어저장', command=self.saveFile)

        self.word_l.grid(column=0, row=0)
        self.meaning_l.grid(column=0, row=1)
        self.word.grid(column=1, row=0)
        self.meaning.grid(column=1, row=1)
        self.saveButton.grid(columnspan=2, row=2)
        self.meaning.bind("<Return>", self.addWordEvent)
        
        self.nw.mainloop()


        # 단어추가하는 로직 
        # 엑셀파일 열기
        # 엔터를 누를 때 이벤트 발생
        # 단어 추가 종료를 누르면 파일 저장

        
         
        
        



if __name__ == '__main__':
    print('토익단어장 실행')
    app = MainWindow()
    app.mainloop()