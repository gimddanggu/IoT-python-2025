from tkinter import *
from tkinter.messagebox import * 
from tkinter.font import *

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
        
    def initComponent(self):
        # 일단 단어 추가 기능만
        self.addWordButton = Button(self, text='단어추가')
        # self.searchWordButton = Button(self, text='단어검색')
        # self.testWordButton = Button(self, text='단어테스트')
        self.addWordButton.pack()
        # self.searchWordButton.pack()
        # self.testWordButton.pack()
        self.word_l = Label(self, text='단어')
        self.meaning_l = Label(self, text='뜻')
        self.word_l.pack()
        self.meaning_l.pack()
        self.word = Entry(self)
        self.meaning = Entry(self)
        self.word.pack()
        self.meaning.pack()





if __name__ =='__main__':
    print('토익단어장 실행')
    app = MainWindow()
    app.mainloop()