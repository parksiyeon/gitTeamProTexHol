from tkinter import *
from tkinter import font
from winsound import *
from player import *
from card import *
import random

class TexasHoldem:
    def __init__(self):
        self.window = Tk()
        self.window.title("Texas Holdem")
        self.window.geometry("800x600")
        self.window.configure(bg="green")
        self.fontstyle = font.Font(self.window, size=24, weight='bold', family='Consolas')
        self.fontstyle2 = font.Font(self.window, size=16, weight='bold', family='Consolas')
        self.setupButton()
        self.setupLabel()

        # 변수들
        self.betMoney=10
        self.cardsphotoimage = [0 for _ in range(10)]
        self.deckN = 0
        self.window.mainloop()

    def setupButton(self):
        self.check = Button(self.window, text="Check", width=6, height=1, font=self.fontstyle2, command=self.pressedCheck)
        self.check.place(x=50, y=500)
        self.Bx1 = Button(self.window, text="Bet x1", width=6, height=1, font=self.fontstyle2, command=self.pressedBet1)
        self.Bx1.place(x=150, y=500)
        self.Bx2 = Button(self.window, text="Bet x2", width=6, height=1, font=self.fontstyle2, command=self.pressedBet2)
        self.Bx2.place(x=250, y=500)
        self.Deal = Button(self.window, text="Deal", width=6, height=1, font=self.fontstyle2, command=self.pressedDeal)
        self.Deal.place(x=600, y=500)
        self.Again = Button(self.window, text="Again", width=6, height=1, font=self.fontstyle2,
                            command=self.pressedAgain)
        self.Again.place(x=700, y=500)
        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'

    def setupLabel(self):
        self.LbetMoney = Label(text="10$", width=4, height=1, font=self.fontstyle, bg="green", fg="cyan")
        self.LbetMoney.place(x=200, y=450)
        self.LplayerMoney = Label(text="You have $1000", width=15, height=1, font=self.fontstyle, bg="green", fg="cyan")
        self.LplayerMoney.place(x=500, y=450)
        self.LplayerPts = Label(text="", width=2, height=1, font=self.fontstyle2, bg="green", fg="white")
        self.LplayerPts.place(x=300, y=300)
        self.LdealerPts = Label(text="", width=2, height=1, font=self.fontstyle2, bg="green", fg="white")
        self.LdealerPts.place(x=300, y=100)
        self.Lstatus = Label(text="", width=15, height=1, font=self.fontstyle, bg="green", fg="white")
        self.Lstatus.place(x=500, y=300)

    def pressedAgain(self):
        pass
    def pressedCheck(self):
        pass
    def pressedBet1(self):
        self.betMoney+=self.betMoney
        self.LbetMoney.configure(text=str(self.betMoney)+"$")
        self.Deal['state'] = 'active'
        self.Deal['bg'] = 'SystemButtonFace'
    def pressedBet2(self):
        self.betMoney += self.betMoney * 2
        self.LbetMoney.configure(text=str(self.betMoney) + "$")
        self.Deal['state'] = 'active'
        self.Deal['bg'] = 'SystemButtonFace'
    def deal(self):
        self.player = Player("player")
        self.dealer = Player("dealer")
        self.cardsphotoimage = [0 for _ in range(10)]
        # 카드 덱 52장 셔플링 0,1,,.51
        self.cardDeck = [i for i in range(52)]
        random.shuffle(self.cardDeck)
        # 딜을 시작하면 버튼 상태가 바뀌어야 하므로 관련 코드 추가
        # 히트와 스테이는 액티브 나머지는 disabled

        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'

        self.check['state'] = 'active'
        self.check['bg'] = 'SystemButtonFace'
        self.Bx1['state'] = 'active'
        self.Bx1['bg'] = 'SystemButtonFace'
        self.Bx2['state'] = 'active'
        self.Bx2['bg'] = 'SystemButtonFace'


    def pressedDeal(self):# 딜 시작
        self.deal()
        self.cardsphotoimage[self.deckN] = Card(self.cardDeck[self.deckN])  # 카드 덱에 저장되어있는 0부터 52까지의 랜덤 숫자를 넘김
        self.player.addCard(self.cardsphotoimage[self.deckN].getValue(), self.cardsphotoimage[self.deckN].filename())
        p = PhotoImage(file='Resources/cards/' + self.player.cards[self.deckN][1])
        self.LcardsPlayer.append(Label(self.window, image=p, bd=0, bg='green'))
        self.LcardsPlayer[self.deckN].image = p
        self.LcardsPlayer[self.deckN].place(x=250 + (self.deckN + 1) * 30, y=350)

        self.deckN += 1
        self.cardsphotoimage[self.deckN] = Card(self.cardDeck[self.deckN])
        self.player.addCard(self.cardsphotoimage[self.deckN].getValue(), self.cardsphotoimage[self.deckN].filename())
        p1 = PhotoImage(file='Resources/cards/' + self.player.cards[self.deckN][1])
        self.LcardsPlayer.append(Label(self.window, image=p1, bd=0, bg='green'))
        self.LcardsPlayer[self.deckN].image = p1
        self.LcardsPlayer[self.deckN].place(x=250 + (self.deckN + 1) * 30, y=350)

    def Check(self):
        pass

TexasHoldem()

