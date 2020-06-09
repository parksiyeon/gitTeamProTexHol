from tkinter import *
from tkinter import font
import tkinter.messagebox

class TermProj:
    def __init__(self):
        self.window = Tk()
        self.window.title("해썹 인증제품 확인")
        self.window.geometry("1000x600")
        self.window.configure(bg="white")
        self.initSearchList()

        self.window.mainloop()

    def initSearchList(self):
        global SearchBox
        self.SearchList = Scrollbar(self.window)
        self.SearchList.pack()
        self.SearchList.place(x=150, y=0)

        TempFont = font.Font(self.window, size=15, weight='bold')
        self.SearchBox = Listbox(self.window, font=TempFont, activestyle='none', width= 12, height=1,borderwidth=7, yscrollcommand= self.SearchList.set)
        self.SearchBox.insert(0, "제품 이름")  #xml에서 제품명
        self.SearchBox.insert(1, "제품 유형")  #xml에서 유형명
        self.SearchBox.pack()
        self.SearchBox.place(x=0, y=0)
        self.SearchList.config(command=self.SearchBox.yview)


TermProj()