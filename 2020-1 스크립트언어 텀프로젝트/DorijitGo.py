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
        self.fontstyle2 = font.Font(self.window, size=12, weight='bold', family='Consolas')

        self.betMoney1 =0
        self.betMoney2 = 0
        self.betMoney3 = 0
        self.playerMoney = 2500
        self.LcardsPlayer1 = []  # 플레이어가 뽑은 카드의 라벨 리스트
        self.LcardsPlayer2 = []
        self.LcardsPlayer3 = []
        self.LcardsDealer = []  # 딜러가 뽑은 카드의 라벨 리스트

        #플레이별 각각 점수 보일 라벨 리스트
        self.LScoresPlayer1=[0 for _ in range(5)]
        self.LScoresPlayer2 = [0 for _ in range(5)]
        self.LScoresPlayer3 = [0 for _ in range(5)]

        self.deckN = 0
        #self.cardsphotoimage = [0 for _ in range(40)] # 20에서 40으로 교체
        self.cardsphotoimage = [0] * 40
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
        self.user1_5milB.place(x=70, y=500)
        self.user1_1milB = Button(self.window, text="1만", width=4, height=1, font=self.fontstyle2, command=self.PressedUser1_1milB)
        self.user1_1milB.place(x=140, y=500)
        self.user2_5milB = Button(self.window, text="5만", width=4, height=1, font=self.fontstyle2, command=self.PressedUser2_5milB)
        self.user2_5milB.place(x=250, y=500)
        self.user2_1milB = Button(self.window, text="1만", width=4, height=1, font=self.fontstyle2, command=self.PressedUser2_1milB)
        self.user2_1milB.place(x=320, y=500)
        self.user3_5milB= Button(self.window, text="5만", width=4, height=1, font=self.fontstyle2, command=self.PressedUser3_5milB)
        self.user3_5milB.place(x=430, y=500)
        self.user3_1milB = Button(self.window, text="1만", width=4, height=1, font=self.fontstyle2, command=self.PressedUser3_1milB)
        self.user3_1milB.place(x=500, y=500)


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
        self.LUserMoney.place(x=605, y=450)
        self.LplayerState = Label(text="", width=12, height=1, font=self.fontstyle2, bg="green", fg="white")
        self.LplayerState.place(x=300, y=350)
        self.LdealerState = Label(text="", width=12, height=1, font=self.fontstyle2, bg="green", fg="white")
        self.LdealerState.place(x=300, y=100)
        self.Lstatus = Label(text="", width=12, height=1, font=self.fontstyle, bg="green", fg="red")
        self.Lstatus.place(x=550, y=350)

        #플레이어 각 화투패 점수 나오는 라 벨,,,,
        for i in range(5):
            self.LScoresPlayer1[i]=Label(text="", width=2, height=1, font=self.fontstyle2, bg="green", fg="white")
            self.LScoresPlayer1[i].place(x=100+i*20,y=250)

            self.LScoresPlayer2[i] = Label(text="", width=2, height=1, font=self.fontstyle2, bg="green", fg="white")
            self.LScoresPlayer2[i].place(x=300 + i * 20, y=250)

            self.LScoresPlayer3[i] = Label(text="", width=2, height=1, font=self.fontstyle2, bg="green", fg="white")
            self.LScoresPlayer3[i].place(x=500 + i * 20, y=250)


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
        #self.cardDeck = [i for i in range(40)]
        self.cardDeck = [0] * 40
        self.inputCardList()
        random.shuffle(self.cardDeck)

    def HitPlayer(self):
        #LcardsPlayer,cardsphotoimage 리스트 인자-->self.deckN
        if self.DealPressedTimes==0:
            self.cardsphotoimage[self.deckN] = Card(self.cardDeck[self.deckN])
            self.player1.addCard(self.cardsphotoimage[self.deckN].getValue(), self.cardsphotoimage[self.deckN].filename(),
                                self.cardsphotoimage[self.deckN].seperatename())
            #print(self.player1.inHand())
            p = PhotoImage(file='GodoriCards/'+self.player1.cards[self.player1.inHand()-1][1])
            self.LcardsPlayer1.append(Label(self.window, image=p, bd=0, bg='green'))
            self.LcardsPlayer1[self.player1.inHand() - 1].image = p
            self.LcardsPlayer1[self.player1.inHand() - 1].place(x=70, y=300)
            self.LScoresPlayer1[self.player1.inHand() - 1].configure(text=str(self.player1.cards[self.player1.inHand() - 1][0]))

            self.deckN+=1
            self.cardsphotoimage[self.deckN] = Card(self.cardDeck[self.deckN])
            self.player2.addCard(self.cardsphotoimage[self.deckN].getValue(), self.cardsphotoimage[self.deckN].filename(),
                                 self.cardsphotoimage[self.deckN].seperatename())
            p = PhotoImage(file='GodoriCards/' + self.player2.cards[self.player2.inHand() - 1][1])
            self.LcardsPlayer2.append(Label(self.window, image=p, bd=0, bg='green'))
            self.LcardsPlayer2[self.player2.inHand() - 1].image = p
            self.LcardsPlayer2[self.player2.inHand() - 1].place(x=270, y=300)
            self.LScoresPlayer2[self.player2.inHand() - 1].configure(text=str(self.player2.cards[self.player2.inHand() - 1][0]))

            self.deckN+=1
            self.cardsphotoimage[self.deckN] = Card(self.cardDeck[self.deckN])
            self.player3.addCard(self.cardsphotoimage[self.deckN].getValue(), self.cardsphotoimage[self.deckN].filename(),
                                 self.cardsphotoimage[self.deckN].seperatename())
            p = PhotoImage(file='GodoriCards/' + self.player3.cards[self.player3.inHand() - 1][1])
            self.LcardsPlayer3.append(Label(self.window, image=p, bd=0, bg='green'))
            self.LcardsPlayer3[self.player3.inHand() - 1].image = p
            self.LcardsPlayer3[self.player3.inHand() - 1].place(x=470, y=300)
            self.LScoresPlayer3[self.player3.inHand() - 1].configure(
                text=str(self.player3.cards[self.player3.inHand() - 1][0]))

        elif self.DealPressedTimes==1:
            for i in range(1, 4):  # p1:471013   p2:581114   p3:691215
                self.deckN += 1
                self.cardsphotoimage[self.deckN] = Card(self.cardDeck[self.deckN])
                self.player1.addCard(self.cardsphotoimage[self.deckN].getValue(),
                                     self.cardsphotoimage[self.deckN].filename(),
                                     self.cardsphotoimage[self.deckN].seperatename())
                # print(self.player1.inHand())
                p = PhotoImage(file='GodoriCards/' + self.player1.cards[self.player1.inHand() - 1][1])
                self.LcardsPlayer1.append(Label(self.window, image=p, bd=0, bg='green'))
                self.LcardsPlayer1[self.player1.inHand() - 1].image = p
                self.LcardsPlayer1[self.player1.inHand() - 1].place(x=70 + i * 30, y=300)  # i*20 >> i* 30
                self.LScoresPlayer1[self.player1.inHand() - 1].configure(
                    text=str(self.player1.cards[self.player1.inHand() - 1][0]))

                self.deckN += 1
                self.cardsphotoimage[self.deckN] = Card(self.cardDeck[self.deckN])
                self.player2.addCard(self.cardsphotoimage[self.deckN].getValue(),
                                     self.cardsphotoimage[self.deckN].filename(),
                                     self.cardsphotoimage[self.deckN].seperatename())
                p = PhotoImage(file='GodoriCards/' + self.player2.cards[self.player2.inHand() - 1][1])
                self.LcardsPlayer2.append(Label(self.window, image=p, bd=0, bg='green'))
                self.LcardsPlayer2[self.player2.inHand() - 1].image = p
                self.LcardsPlayer2[self.player2.inHand() - 1].place(x=280 + i * 30, y=300)  # i*20 >> i* 30
                self.LScoresPlayer2[self.player2.inHand() - 1].configure(
                    text=str(self.player2.cards[self.player2.inHand() - 1][0]))

                self.deckN += 1
                self.cardsphotoimage[self.deckN] = Card(self.cardDeck[self.deckN])
                self.player3.addCard(self.cardsphotoimage[self.deckN].getValue(),
                                     self.cardsphotoimage[self.deckN].filename(),
                                     self.cardsphotoimage[self.deckN].seperatename())
                p = PhotoImage(file='GodoriCards/' + self.player3.cards[self.player3.inHand() - 1][1])
                self.LcardsPlayer3.append(Label(self.window, image=p, bd=0, bg='green'))
                self.LcardsPlayer3[self.player3.inHand() - 1].image = p
                self.LcardsPlayer3[self.player3.inHand() - 1].place(x=480 + i * 30, y=300)  # i*20 >> i* 30
                self.LScoresPlayer3[self.player3.inHand() - 1].configure(
                    text=str(self.player3.cards[self.player3.inHand() - 1][0]))

        elif self.DealPressedTimes==2:
            self.deckN += 1
            self.cardsphotoimage[self.deckN] = Card(self.cardDeck[self.deckN])
            self.player1.addCard(self.cardsphotoimage[self.deckN].getValue(),
                                 self.cardsphotoimage[self.deckN].filename(),
                                 self.cardsphotoimage[self.deckN].seperatename())
            # print(self.player1.inHand())
            p = PhotoImage(file='GodoriCards/' + self.player1.cards[self.player1.inHand() - 1][1])
            self.LcardsPlayer1.append(Label(self.window, image=p, bd=0, bg='green'))
            self.LcardsPlayer1[self.player1.inHand() - 1].image = p
            self.LcardsPlayer1[self.player1.inHand() - 1].place(x=190, y=300)  # i*20 >> i* 30
            self.LScoresPlayer1[self.player1.inHand() - 1].configure(
                text=str(self.player1.cards[self.player1.inHand() - 1][0]))

            self.deckN += 1
            self.cardsphotoimage[self.deckN] = Card(self.cardDeck[self.deckN])
            self.player2.addCard(self.cardsphotoimage[self.deckN].getValue(),
                                 self.cardsphotoimage[self.deckN].filename(),
                                 self.cardsphotoimage[self.deckN].seperatename())
            p = PhotoImage(file='GodoriCards/' + self.player2.cards[self.player2.inHand() - 1][1])
            self.LcardsPlayer2.append(Label(self.window, image=p, bd=0, bg='green'))
            self.LcardsPlayer2[self.player2.inHand() - 1].image = p
            self.LcardsPlayer2[self.player2.inHand() - 1].place(x=400, y=300)  # i*20 >> i* 30
            self.LScoresPlayer2[self.player2.inHand() - 1].configure(
                text=str(self.player2.cards[self.player2.inHand() - 1][0]))

            self.deckN += 1
            self.cardsphotoimage[self.deckN] = Card(self.cardDeck[self.deckN])
            self.player3.addCard(self.cardsphotoimage[self.deckN].getValue(),
                                 self.cardsphotoimage[self.deckN].filename(),
                                 self.cardsphotoimage[self.deckN].seperatename())
            p = PhotoImage(file='GodoriCards/' + self.player3.cards[self.player3.inHand() - 1][1])
            self.LcardsPlayer3.append(Label(self.window, image=p, bd=0, bg='green'))
            self.LcardsPlayer3[self.player3.inHand() - 1].image = p
            self.LcardsPlayer3[self.player3.inHand() - 1].place(x=600, y=300)  # i*20 >> i* 30
            self.LScoresPlayer3[self.player3.inHand() - 1].configure(
                text=str(self.player3.cards[self.player3.inHand() - 1][0]))

    def HitDealer(self):
        if self.DealPressedTimes==0:
            self.deckN += 1  # 가려진 카드
            self.cardsphotoimage[self.deckN] = Card(self.cardDeck[self.deckN])
            self.dealer.addCard(self.cardsphotoimage[self.deckN].getValue(), self.cardsphotoimage[self.deckN].filename(),
                                self.cardsphotoimage[self.deckN].seperatename())
            p = PhotoImage(file='GodoriCards/cardback.gif')  # 카드 가려줄 뒷면 이미지! 추후 지워짐(리스트에 추가할필요 없음)
            self.LcardsDealer.append(Label(self.window, image=p, bd=0, bg='green'))
            self.LcardsDealer[self.dealer.inHand() - 1].image = p
            self.LcardsDealer[self.dealer.inHand() - 1].place(x=270, y=100)

        elif self.DealPressedTimes==1:
            for i in range(3):
                self.deckN += 1  # 가려진 카드
                self.cardsphotoimage[self.deckN] = Card(self.cardDeck[self.deckN])
                self.dealer.addCard(self.cardsphotoimage[self.deckN].getValue(),
                                    self.cardsphotoimage[self.deckN].filename(),
                                    self.cardsphotoimage[self.deckN].seperatename())
                p = PhotoImage(file='GodoriCards/cardback.gif')  # 카드 가려줄 뒷면 이미지! 추후 지워짐(리스트에 추가할필요 없음)
                self.LcardsDealer.append(Label(self.window, image=p, bd=0, bg='green'))
                self.LcardsDealer[self.dealer.inHand() - 1].image = p
                self.LcardsDealer[self.dealer.inHand() - 1].place(x=290 + i * 30, y=100)  # i*20 >> i* 30

        elif self.DealPressedTimes==2:
            self.deckN += 1  # 가려진 카드
            self.cardsphotoimage[self.deckN] = Card(self.cardDeck[self.deckN])
            self.dealer.addCard(self.cardsphotoimage[self.deckN].getValue(),
                                self.cardsphotoimage[self.deckN].filename(),
                                self.cardsphotoimage[self.deckN].seperatename())
            p = PhotoImage(file='GodoriCards/cardback.gif')  # 카드 가려줄 뒷면 이미지! 추후 지워짐(리스트에 추가할필요 없음)
            self.LcardsDealer.append(Label(self.window, image=p, bd=0, bg='green'))
            self.LcardsDealer[self.dealer.inHand() - 1].image = p
            self.LcardsDealer[self.dealer.inHand() - 1].place(x=380, y=100)


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

        if self.DealPressedTimes==2:
            self.Opendealercard()

        self.DealPressedTimes+=1

    def Opendealercard(self):
        print(self.dealer.inHand()-1)
        for i in range(5):
            p = PhotoImage(file='GodoriCards/' + self.dealer.cards[i][1])
            self.LcardsDealer[i].configure(image=p)  # 이미지 레퍼런스 변경
            self.LcardsDealer[i].image = p  # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
            #self.LdealerState.configure(text=str(self.dealer.value()))
        #self.CheckWinner()

    def PressedAgain(self):
        self.cardDeck.clear()
        self.deckN = 0
        self.pstatevalue = 0
        self.dstatevalue = 0
        self.DealPressedTimes=0
        self.betMoney1=0
        self.betMoney2=0
        self.betMoney3=0

        self.StartButtonState()
        self.LplayerState.configure(text="")
        self.LdealerState.configure(text="")
        self.Lstatus.configure(text="")
        self.Lstatus.configure(text="")
        self.LUser1_betMoney.configure(text="")
        self.LUser2_betMoney.configure(text="")
        self.LUser3_betMoney.configure(text="")

        del self.player1
        del self.player2
        del self.player3
        del self.dealer

        for i in range(5):
            self.LcardsPlayer1[i].configure(image='')
            self.LcardsPlayer2[i].configure(image='')
            self.LcardsPlayer3[i].configure(image='')
            self.LcardsDealer[i].configure(image='')
            self.LScoresPlayer1[i].configure(text="")
            self.LScoresPlayer2[i].configure(text="")
            self.LScoresPlayer3[i].configure(text="")

        self.LcardsPlayer1.clear()
        self.LcardsPlayer2.clear()
        self.LcardsPlayer3.clear()
        self.LcardsDealer.clear()

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

    def inputCardList(self):
        n = 0
        for i in range(10, 101, 10):
            for j in range(1, 5):
                self.cardDeck[n] = i+j
                n += 1

    def checkCardtable(self): #족보 써둠
        cardtable = [[1,1,8,'콩콩팔'],
                     [1,2,7,'삐리칠'],
                     [1,3,6,'물삼육'],
                     [1,4,5,'빽새오'],
                     [1,9,10,'삥구장'],
                     [2,2,6,'니니육'],
                     [2,3,5,'이삼오'],
                     [2,8,10,'이판장'],
                     [3,3,4,'심심새'],
                     [3,7,10,'삼칠장'],
                     [3,8,9,'삼빡구'],
                     [4,4,2,'살살이'],
                     [4,6,10,'사륙장'],
                     [4,8,9,'사칠구'],
                     [5,5,10,'꼬꼬장'],
                     [5,6,9,'오륙구'],
                     [5,7,8,'오리발'],
                     [6,6,8,'쭉쭉팔'],
                     [7,7,6,'철철육'],
                     [8,8,4,'팍팍싸'],
                     [9,9,2,'구구리']]

        # 3장을 메이르도 완성한 뒤 나머지 2장으로 족보 비교

        # 1순위 - 2장 self.value가 3,8 >> 38광땡
        # 2순위 - self.value가 1,3 또는 1,8 >> 광땡
        # 3순위 - self.value가 같을 때 >> 땡 (월이 높을 수록 높은 족보)
        # 4순위 - 1,2,3 순위 해당x 두 패의 숫자 합이 1~8 >> 끗
        # 5순위 - 2,8월 또는 3,7월 끗 수가 0 >> 가장 낮음


DorijitGo()