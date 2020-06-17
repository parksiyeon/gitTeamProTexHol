from tkinter import *
from tkinter import font
from CCard import *
from Cplayer import *
import random


class DorijitGo:
    def __init__(self):
        self.window = Tk()
        self.window.title("도리짓고땡")
        self.window.geometry("800x600")
        self.window.configure(bg="green")

        self.bg = PhotoImage(file='GodoriCards/table.gif')
        self.gamebg = Label(image=self.bg)
        self.gamebg.place(x=0, y=0)

        self.fontstyle = font.Font(self.window, size=24, weight='bold', family='Consolas')
        self.fontstyle2 = font.Font(self.window, size=16, weight='bold', family='Consolas')

        self.betMoney1 =0
        self.betMoney2 = 0
        self.betMoney3 = 0
        self.playerMoney = 2500
        self.LcardsPlayer1 = []  # 플레이어가 뽑은 카드의 라벨 리스트
        self.LcardsPlayer2 = []
        self.LcardsPlayer3 = []
        self.LcardsDealer = []  # 딜러가 뽑은 카드의 라벨 리스트
        self.deckN = 0
        self.cardsphotoimage = [0 for _ in range(40)] # 20에서 40으로 교체
        self.pstatevalue = 0
        self.dstatevalue = 0

        self.pCheck = 0
        self.dCheck = 0

        self.DealPressedTimes=0

        self.setupButton()
        self.setupLabel()
        self.StartButtonState()
        self.window.mainloop()

    def setupButton(self):
        self.user1_5milB = Button(self.window, text="5만", width=4, height=1, font=self.fontstyle2, command=self.PressedUser1_5milB)
        self.user1_5milB.place(x=50, y=500)
        self.user1_1milB = Button(self.window, text="1만", width=4, height=1, font=self.fontstyle2, command=self.PressedUser1_1milB)
        self.user1_1milB.place(x=120, y=500)
        self.user2_5milB = Button(self.window, text="5만", width=4, height=1, font=self.fontstyle2, command=self.PressedUser2_5milB)
        self.user2_5milB.place(x=230, y=500)
        self.user2_1milB = Button(self.window, text="1만", width=4, height=1, font=self.fontstyle2, command=self.PressedUser2_1milB)
        self.user2_1milB.place(x=300, y=500)
        self.user3_5milB= Button(self.window, text="5만", width=4, height=1, font=self.fontstyle2, command=self.PressedUser3_5milB)
        self.user3_5milB.place(x=410, y=500)
        self.user3_1milB = Button(self.window, text="1만", width=4, height=1, font=self.fontstyle2, command=self.PressedUser3_1milB)
        self.user3_1milB.place(x=480, y=500)


        self.Deal = Button(self.window, text="Deal", width=6, height=1, font=self.fontstyle2, command=self.PressedDeal)
        self.Deal.place(x=600, y=500)
        self.Again = Button(self.window, text="Again", width=6, height=1, font=self.fontstyle2,
                            command=self.PressedAgain)
        self.Again.place(x=700, y=500)

    def setupLabel(self):
        self.LUser1_betMoney = Label(text="0만", width=4, height=1, font=self.fontstyle, bg="green", fg="orange")
        self.LUser1_betMoney.place(x=85, y=450)
        self.LUser2_betMoney = Label(text="0만", width=4, height=1, font=self.fontstyle, bg="green", fg="orange")
        self.LUser2_betMoney.place(x=260, y=450)
        self.LUser3_betMoney = Label(text="0만", width=4, height=1, font=self.fontstyle, bg="green", fg="orange")
        self.LUser3_betMoney.place(x=450, y=450)


        self.LUserMoney = Label(text="2500만", width=8, height=1, font=self.fontstyle, bg="green",
                                fg="orange")
        self.LUserMoney.place(x=630, y=450)
        self.LplayerState = Label(text="", width=12, height=1, font=self.fontstyle2, bg="green", fg="white")
        self.LplayerState.place(x=300, y=350)
        self.LdealerState = Label(text="", width=12, height=1, font=self.fontstyle2, bg="green", fg="white")
        self.LdealerState.place(x=300, y=100)
        self.Lstatus = Label(text="", width=12, height=1, font=self.fontstyle, bg="green", fg="red")
        self.Lstatus.place(x=550, y=350)

    def PressedUser1_5milB(self):
        self.betMoney1+=5
        self.playerMoney -=5
        self.LUser1_betMoney.configure(text=str(self.betMoney1)+"만")
        self.LUserMoney.configure(text=str(self.playerMoney)+"만")
        #PlaySound('GodoriCards/', SND_FILENAME)

    def PressedUser2_5milB(self):
        self.betMoney2+=5
        self.playerMoney -=5
        self.LUser2_betMoney.configure(text=str(self.betMoney2)+"만")
        self.LUserMoney.configure(text=str(self.playerMoney)+"만")
        #PlaySound('GodoriCards/', SND_FILENAME)

    def PressedUser3_5milB(self):
        self.betMoney3+=5
        self.playerMoney-= 5
        self.LUser3_betMoney.configure(text=str(self.betMoney3)+"만")
        self.LUserMoney.configure(text=str(self.playerMoney)+"만")
        #PlaySound('GodoriCards/', SND_FILENAME)

    def PressedUser1_1milB(self):
        self.betMoney1+=1
        self.playerMoney -= 1
        self.LUser1_betMoney.configure(text=str(self.betMoney1) + "만")
        self.LUserMoney.configure(text=str(self.playerMoney)+"만")
        #PlaySound('GodoriCards/', SND_FILENAME)

    def PressedUser2_1milB(self):
        self.betMoney2+=1
        self.playerMoney -= 1
        self.LUser2_betMoney.configure(text=str(self.betMoney2) + "만")
        self.LUserMoney.configure(text=str(self.playerMoney)+"만")
        #PlaySound('GodoriCards/', SND_FILENAME)

    def PressedUser3_1milB(self):
        self.betMoney3+=1
        self.playerMoney -= 1
        self.LUser3_betMoney.configure(text=str(self.betMoney3) + "만")
        self.LUserMoney.configure(text=str(self.playerMoney)+"만")
        #PlaySound('GodoriCards/', SND_FILENAME)

    def StartGame(self):  # 딜 처음 시작 때 불리는 세팅 함수
        self.player1 = Player("player1")
        self.player2 = Player("player2")
        self.player3 = Player("player3")
        self.dealer = Player("dealer")
        # 화투 패 40장 셔플링 0,1,,.40
        self.cardDeck = [i for i in range(40)]
        random.shuffle(self.cardDeck)

    def HitPlayer(self):
        #LcardsPlayer,cardsphotoimage 리스트 인자-->self.deckN

        self.cardsphotoimage[self.deckN] = Card(self.cardDeck[self.deckN])
        self.player1.addCard(self.cardsphotoimage[self.deckN].getValue(), self.cardsphotoimage[self.deckN].filename(),
                            self.cardsphotoimage[self.deckN].seperatename())
        #print(self.player1.inHand())
        p = PhotoImage(file='GodoriCards/'+self.player1.cards[self.player1.inHand()-1][1])
        self.LcardsPlayer1.append(Label(self.window, image=p, bd=0, bg='green'))
        self.LcardsPlayer1[self.player1.inHand() - 1].image = p
        self.LcardsPlayer1[self.player1.inHand() - 1].place(x=70, y=300)

        self.deckN+=1
        self.cardsphotoimage[self.deckN] = Card(self.cardDeck[self.deckN])
        self.player2.addCard(self.cardsphotoimage[self.deckN].getValue(), self.cardsphotoimage[self.deckN].filename(),
                             self.cardsphotoimage[self.deckN].seperatename())
        p1 = PhotoImage(file='GodoriCards/' + self.player2.cards[self.player2.inHand() - 1][1])
        self.LcardsPlayer2.append(Label(self.window, image=p1, bd=0, bg='green'))
        self.LcardsPlayer2[self.player2.inHand() - 1].image = p1
        self.LcardsPlayer2[self.player2.inHand() - 1].place(x=270, y=300)

        self.deckN+=1
        self.cardsphotoimage[self.deckN] = Card(self.cardDeck[self.deckN])
        self.player3.addCard(self.cardsphotoimage[self.deckN].getValue(), self.cardsphotoimage[self.deckN].filename(),
                             self.cardsphotoimage[self.deckN].seperatename())
        p2 = PhotoImage(file='GodoriCards/' + self.player3.cards[self.player3.inHand() - 1][1])
        self.LcardsPlayer3.append(Label(self.window, image=p2, bd=0, bg='green'))
        self.LcardsPlayer3[self.player3.inHand() - 1].image = p2
        self.LcardsPlayer3[self.player3.inHand() - 1].place(x=470, y=300)

    def AllCardstoPlayer(self):#3명의 플레이어에게 총 4장까지 카드 분배해주는 함수
        for i in range(1,5): #p1:471013   p2:581114   p3:691215
            self.deckN+=1
            self.cardsphotoimage[self.deckN] = Card(self.cardDeck[self.deckN])
            self.player1.addCard(self.cardsphotoimage[self.deckN].getValue(), self.cardsphotoimage[self.deckN].filename(),
                                 self.cardsphotoimage[self.deckN].seperatename())
            # print(self.player1.inHand())
            p = PhotoImage(file='GodoriCards/' + self.player1.cards[self.player1.inHand() - 1][1])
            self.LcardsPlayer1.append(Label(self.window, image=p, bd=0, bg='green'))
            self.LcardsPlayer1[self.player1.inHand() - 1].image = p
            self.LcardsPlayer1[self.player1.inHand() - 1].place(x=70+i*20, y=300)

            self.deckN += 1
            self.cardsphotoimage[self.deckN] = Card(self.cardDeck[self.deckN])
            self.player2.addCard(self.cardsphotoimage[self.deckN].getValue(), self.cardsphotoimage[self.deckN].filename(),
                                 self.cardsphotoimage[self.deckN].seperatename())
            p1 = PhotoImage(file='GodoriCards/' + self.player2.cards[self.player2.inHand() - 1][1])
            self.LcardsPlayer2.append(Label(self.window, image=p1, bd=0, bg='green'))
            self.LcardsPlayer2[self.player2.inHand() - 1].image = p1
            self.LcardsPlayer2[self.player2.inHand() - 1].place(x=280+i*20, y=300)

            self.deckN += 1
            self.cardsphotoimage[self.deckN] = Card(self.cardDeck[self.deckN])
            self.player3.addCard(self.cardsphotoimage[self.deckN].getValue(), self.cardsphotoimage[self.deckN].filename(),
                                 self.cardsphotoimage[self.deckN].seperatename())
            p2 = PhotoImage(file='GodoriCards/' + self.player3.cards[self.player3.inHand() - 1][1])
            self.LcardsPlayer3.append(Label(self.window, image=p2, bd=0, bg='green'))
            self.LcardsPlayer3[self.player3.inHand() - 1].image = p2
            self.LcardsPlayer3[self.player3.inHand() - 1].place(x=480+i*20, y=300)

    def AllCardstoDealer(self):
        for i in range(4):
            self.deckN += 1  # 가려진 카드
            self.cardsphotoimage[self.deckN] = Card(self.cardDeck[self.deckN])
            self.dealer.addCard(self.cardsphotoimage[self.deckN].getValue(), self.cardsphotoimage[self.deckN].filename(),
                                self.cardsphotoimage[self.deckN].seperatename())
            p = PhotoImage(file='GodoriCards/cardback.gif')  # 카드 가려줄 뒷면 이미지! 추후 지워짐(리스트에 추가할필요 없음)
            self.LcardsDealer.append(Label(self.window, image=p, bd=0, bg='green'))
            self.LcardsDealer[self.dealer.inHand() - 1].image = p
            self.LcardsDealer[self.dealer.inHand() - 1].place(x=290+i*20, y=100)

    def HitDealer(self):
        self.deckN += 1  # 가려진 카드
        self.cardsphotoimage[self.deckN] = Card(self.cardDeck[self.deckN])
        self.dealer.addCard(self.cardsphotoimage[self.deckN].getValue(), self.cardsphotoimage[self.deckN].filename(),
                            self.cardsphotoimage[self.deckN].seperatename())
        p = PhotoImage(file='GodoriCards/cardback.gif')  # 카드 가려줄 뒷면 이미지! 추후 지워짐(리스트에 추가할필요 없음)
        self.LcardsDealer.append(Label(self.window, image=p, bd=0, bg='green'))
        self.LcardsDealer[self.dealer.inHand() - 1].image = p
        self.LcardsDealer[self.dealer.inHand() - 1].place(x=270, y=100)

    def StartButtonState(self):
        self.user1_5milB['state'] = 'disabled'
        self.user1_5milB['bg'] = 'gray'
        self.user1_1milB['state'] =  'disabled'
        self.user1_1milB['bg'] = 'gray'
        self.user2_5milB['state'] = 'disabled'
        self.user2_5milB['bg'] = 'gray'
        self.user2_1milB['state'] = 'disabled'
        self.user2_1milB['bg'] = 'gray'
        self.user3_5milB['state'] = 'disabled'
        self.user3_5milB['bg'] = 'gray'
        self.user3_1milB['state'] = 'disabled'
        self.user3_1milB['bg'] = 'gray'

        self.Deal['state'] = 'active'
        self.Deal['bg'] = 'SystemButtonFace'
        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'

    def ChangeButtonState(self):
        if self.DealPressedTimes==2:
            self.user1_5milB['state'] = 'disabled'
            self.user1_5milB['bg'] = 'gray'
            self.user1_1milB['state'] = 'disabled'
            self.user1_1milB['bg'] = 'gray'
            self.user2_5milB['state'] = 'disabled'
            self.user2_5milB['bg'] = 'gray'
            self.user2_1milB['state'] = 'disabled'
            self.user2_1milB['bg'] = 'gray'
            self.user3_5milB['state'] = 'disabled'
            self.user3_5milB['bg'] = 'gray'
            self.user3_1milB['state'] = 'disabled'
            self.user3_1milB['bg'] = 'gray'
            self.Deal['state'] ='disabled'
            self.Deal['bg'] = 'gray'
            self.Again['state'] ='active'
            self.Again['bg'] ='SystemButtonFace'

        else:
            self.user1_5milB['state'] = 'active'
            self.user1_5milB['bg'] = 'SystemButtonFace'
            self.user1_1milB['state'] = 'active'
            self.user1_1milB['bg'] = 'SystemButtonFace'
            self.user2_5milB['state'] = 'active'
            self.user2_5milB['bg'] = 'SystemButtonFace'
            self.user2_1milB['state'] = 'active'
            self.user2_1milB['bg'] = 'SystemButtonFace'
            self.user3_5milB['state'] = 'active'
            self.user3_5milB['bg'] = 'SystemButtonFace'
            self.user3_1milB['state'] = 'active'
            self.user3_1milB['bg'] = 'SystemButtonFace'


    def PressedDeal(self):
        if self.DealPressedTimes==0:
            self.StartGame()
            self.HitPlayer()
            self.HitDealer()
            self.ChangeButtonState()

        elif self.DealPressedTimes==1:
            self.AllCardstoPlayer()
            self.AllCardstoDealer()
        elif self.DealPressedTimes==2: #결과확인
            self.Opendealercard()
            self.ChangeButtonState()

        self.DealPressedTimes+=1

    def Opendealercard(self):
        for i in range(5):
            p = PhotoImage(file='GodoriCards/' + self.dealer.cards[i][1])
            self.LcardsDealer[i].configure(image=p)  # 이미지 레퍼런스 변경
            self.LcardsDealer[i].image = p  # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
            #self.LdealerState.configure(text=str(self.dealer.value()))
        #self.CheckWinner()

    def PressedAgain(self):
        self.cardDeck.clear()
        self.deckN = 0
        self.commoncardsN = 0
        self.pstatevalue = 0
        self.dstatevalue = 0

        self.setupButton()
        self.LplayerState.configure(text="")
        self.LdealerState.configure(text="")
        self.Lstatus.configure(text="")
        self.Lstatus.configure(text="")

        del self.player1
        del self.player2
        del self.player3
        del self.dealer

        # for i in range(2):
        #     self.LcardsPlayer[i].configure(image='')
        #     self.LcardsDealer[i].configure(image='')
        # for i in range(5):
        #     self.LcardsCommon[i].configure(image='')
        #
        # self.LcardsPlayer.clear()
        # self.LcardsDealer.clear()
        # self.LcardsCommon.clear()

    def CheckWinner(self):
        self.LUserMoney.configure(text="" + str(self.playerMoney))
        self.user1_5milB['state'] = 'disabled'
        self.user1_5milB['bg'] = 'gray'
        self.user1_5milB['state'] = 'disabled'
        self.user1_5milB['bg'] = 'gray'
        self.user2_5milB['state'] = 'disabled'
        self.user2_5milB['bg'] = 'gray'
        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'active'
        self.Again['bg'] = 'SystemButtonFace'

        self.pCheck = self.PlayerCheck()
        self.dCheck = self.DealerCheck()

        if self.pCheck > self.dCheck:
            #PlaySound('Resources/sounds/win.wav', SND_FILENAME)
            self.Lstatus.configure(text="Win")
            self.playerMoney += self.betMoney

        elif self.pCheck == self.dCheck:
            if self.pstatevalue > self.dstatevalue:
                self.Lstatus.configure(text="Win")
                #PlaySound('Resources/sounds/win.wav', SND_FILENAME)
            elif self.pstatevalue == self.dstatevalue:
                self.Lstatus.configure(text="Push")
            else:
                self.Lstatus.configure(text="Lose")
                #PlaySound('Resources/sounds/wrong.wav', SND_FILENAME)
            self.playerMoney = self.playerMoney

        else:
            #PlaySound('Resources/sounds/wrong.wav', SND_FILENAME)
            self.Lstatus.configure(text="Lose")
            self.playerMoney -= self.betMoney

        self.LUserMoney.configure(text= str(self.playerMoney))
        self.betMoney = 10
        self.LUser1_betMoney.configure(text="$" + str(self.betMoney))

    def PlayerCheck(self):  # 플레이어의 상태를 체크 한 당
        pass

    def DealerCheck(self):
        pass

DorijitGo()