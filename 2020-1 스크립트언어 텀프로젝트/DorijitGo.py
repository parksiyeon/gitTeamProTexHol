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

        self.cardtable = [[1, 1, 8, '콩콩팔'],
                          [1, 2, 7, '삐리칠'],
                          [1, 3, 6, '물삼육'],
                          [1, 4, 5, '빽새오'],
                          [1, 9, 10, '삥구장'],
                          [2, 2, 6, '니니육'],
                          [2, 3, 5, '이삼오'],
                          [2, 8, 10, '이판장'],
                          [3, 3, 4, '심심새'],
                          [3, 7, 10, '삼칠장'],
                          [3, 8, 9, '삼빡구'], #10
                          [2, 4, 4, '살살이'],
                          [4, 6, 10, '사륙장'],
                          [4, 7, 9, '사칠구'],
                          [5, 5, 10, '꼬꼬장'],
                          [5, 6, 9, '오륙구'],
                          [5, 7, 8, '오리발'],
                          [6, 6, 8, '쭉쭉팔'],
                          [7, 7, 6, '철철육'],
                          [8, 8, 4, '팍팍싸'],
                          [9, 9, 2, '구구리']]

        #플레이별 각각 점수 보일 라벨 리스트
        self.LScoresPlayer1=[0 for _ in range(5)]
        self.LScoresPlayer2 = [0 for _ in range(5)]
        self.LScoresPlayer3 = [0 for _ in range(5)]
        self.LScoresDealer=[0 for _ in range(5)]

        self.deckN = 0
        #self.cardsphotoimage = [0 for _ in range(40)] # 20에서 40으로 교체
        self.cardsphotoimage = [0] * 40
        self.pstatevalue = 0
        self.dstatevalue = 0

        self.pCheck = 0
        self.dCheck = 0

        self.playerFlag1 = 0
        self.playerFlag2 = 0
        self.playerFlag3 = 0
        self.playerFlagD = 0

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

        self.Lplayer1State = Label(text="", width=8, height=1, font=self.fontstyle2, bg="green", fg="white")
        self.Lplayer1State.place(x=100, y=400)
        self.Lplayer2State = Label(text="", width=8, height=1, font=self.fontstyle2, bg="green", fg="white")
        self.Lplayer2State.place(x=300, y=400)
        self.Lplayer3State = Label(text="", width=8, height=1, font=self.fontstyle2, bg="green", fg="white")
        self.Lplayer3State.place(x=500, y=400)
        self.LdealerState = Label(text="", width=8, height=1, font=self.fontstyle2, bg="green", fg="white")
        self.LdealerState.place(x=500, y=100)

        #메이드 뒤에 붙는 애들
        self.Lplayer1StateJB=Label(text="",width=8,height=1,font=self.fontstyle2,bg="green", fg="white")
        self.Lplayer1StateJB.place(x=170,y=400)
        self.Lplayer2StateJB = Label(text="", width=8, height=1,font=self.fontstyle2, bg="green", fg="white")
        self.Lplayer2StateJB.place(x=370, y=400)
        self.Lplayer3StateJB = Label(text="", width=8, height=1,font=self.fontstyle2, bg="green", fg="white")
        self.Lplayer3StateJB.place(x=570, y=400)
        self.LdealerStateJB = Label(text="", width=8, height=1,font=self.fontstyle2, bg="green", fg="white")
        self.LdealerStateJB.place(x=570, y=100)

        #플레이어 각 화투패 점수 나오는 라 벨,,,,
        for i in range(5):
            self.LScoresPlayer1[i]=Label(text="", width=2, height=1, font=self.fontstyle2, bg="green", fg="white")
            self.LScoresPlayer1[i].place(x=100+i*20,y=250)

            self.LScoresPlayer2[i] = Label(text="", width=2, height=1, font=self.fontstyle2, bg="green", fg="white")
            self.LScoresPlayer2[i].place(x=300 + i * 20, y=250)

            self.LScoresPlayer3[i] = Label(text="", width=2, height=1, font=self.fontstyle2, bg="green", fg="white")
            self.LScoresPlayer3[i].place(x=500 + i * 20, y=250)

            self.LScoresDealer[i] = Label(text="", width=2, height=1, font=self.fontstyle2, bg="green", fg="white")
            self.LScoresDealer[i].place(x=500 + i * 20, y=50)

        #승/패 라벨
        self.resultLabel1 = Label(text="", width=2, height=1, font=self.fontstyle2, bg="green", fg="white")
        self.resultLabel1.place(x=205, y=250)
        self.resultLabel2 = Label(text="", width=2, height=1, font=self.fontstyle2, bg="green", fg="white")
        self.resultLabel2.place(x=405, y=250)
        self.resultLabel3 = Label(text="", width=2, height=1, font=self.fontstyle2, bg="green", fg="white")
        self.resultLabel3.place(x=605, y=250)


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
            self.player1.addCard(self.cardsphotoimage[self.deckN].getValue(), self.cardsphotoimage[self.deckN].filename())
            #print(self.player1.inHand())
            p = PhotoImage(file='GodoriCards/'+self.player1.cards[self.player1.inHand()-1][1])
            self.LcardsPlayer1.append(Label(self.window, image=p, bd=0, bg='green'))
            self.LcardsPlayer1[self.player1.inHand() - 1].image = p
            self.LcardsPlayer1[self.player1.inHand() - 1].place(x=70, y=300)
            self.LScoresPlayer1[self.player1.inHand() - 1].configure(text=str(self.player1.cards[self.player1.inHand() - 1][0]))

            self.deckN+=1
            self.cardsphotoimage[self.deckN] = Card(self.cardDeck[self.deckN])
            self.player2.addCard(self.cardsphotoimage[self.deckN].getValue(), self.cardsphotoimage[self.deckN].filename())
            p = PhotoImage(file='GodoriCards/' + self.player2.cards[self.player2.inHand() - 1][1])
            self.LcardsPlayer2.append(Label(self.window, image=p, bd=0, bg='green'))
            self.LcardsPlayer2[self.player2.inHand() - 1].image = p
            self.LcardsPlayer2[self.player2.inHand() - 1].place(x=270, y=300)
            self.LScoresPlayer2[self.player2.inHand() - 1].configure(text=str(self.player2.cards[self.player2.inHand() - 1][0]))

            self.deckN+=1
            self.cardsphotoimage[self.deckN] = Card(self.cardDeck[self.deckN])
            self.player3.addCard(self.cardsphotoimage[self.deckN].getValue(), self.cardsphotoimage[self.deckN].filename())
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
                                     self.cardsphotoimage[self.deckN].filename())
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
                                     self.cardsphotoimage[self.deckN].filename())
                p = PhotoImage(file='GodoriCards/' + self.player2.cards[self.player2.inHand() - 1][1])
                self.LcardsPlayer2.append(Label(self.window, image=p, bd=0, bg='green'))
                self.LcardsPlayer2[self.player2.inHand() - 1].image = p
                self.LcardsPlayer2[self.player2.inHand() - 1].place(x=280 + i * 30, y=300)  # i*20 >> i* 30
                self.LScoresPlayer2[self.player2.inHand() - 1].configure(
                    text=str(self.player2.cards[self.player2.inHand() - 1][0]))

                self.deckN += 1
                self.cardsphotoimage[self.deckN] = Card(self.cardDeck[self.deckN])
                self.player3.addCard(self.cardsphotoimage[self.deckN].getValue(),
                                     self.cardsphotoimage[self.deckN].filename())
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
                                 self.cardsphotoimage[self.deckN].filename())
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
                                 self.cardsphotoimage[self.deckN].filename())
            p = PhotoImage(file='GodoriCards/' + self.player2.cards[self.player2.inHand() - 1][1])
            self.LcardsPlayer2.append(Label(self.window, image=p, bd=0, bg='green'))
            self.LcardsPlayer2[self.player2.inHand() - 1].image = p
            self.LcardsPlayer2[self.player2.inHand() - 1].place(x=400, y=300)  # i*20 >> i* 30
            self.LScoresPlayer2[self.player2.inHand() - 1].configure(
                text=str(self.player2.cards[self.player2.inHand() - 1][0]))

            self.deckN += 1
            self.cardsphotoimage[self.deckN] = Card(self.cardDeck[self.deckN])
            self.player3.addCard(self.cardsphotoimage[self.deckN].getValue(),
                                 self.cardsphotoimage[self.deckN].filename())
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
            self.dealer.addCard(self.cardsphotoimage[self.deckN].getValue(), self.cardsphotoimage[self.deckN].filename())
            p = PhotoImage(file='GodoriCards/cardback.gif')  # 카드 가려줄 뒷면 이미지! 추후 지워짐(리스트에 추가할필요 없음)
            self.LcardsDealer.append(Label(self.window, image=p, bd=0, bg='green'))
            self.LcardsDealer[self.dealer.inHand() - 1].image = p
            self.LcardsDealer[self.dealer.inHand() - 1].place(x=270, y=100)

        elif self.DealPressedTimes==1:
            for i in range(3):
                self.deckN += 1  # 가려진 카드
                self.cardsphotoimage[self.deckN] = Card(self.cardDeck[self.deckN])
                self.dealer.addCard(self.cardsphotoimage[self.deckN].getValue(),
                                    self.cardsphotoimage[self.deckN].filename())
                p = PhotoImage(file='GodoriCards/cardback.gif')  # 카드 가려줄 뒷면 이미지! 추후 지워짐(리스트에 추가할필요 없음)
                self.LcardsDealer.append(Label(self.window, image=p, bd=0, bg='green'))
                self.LcardsDealer[self.dealer.inHand() - 1].image = p
                self.LcardsDealer[self.dealer.inHand() - 1].place(x=290 + i * 30, y=100)  # i*20 >> i* 30

        elif self.DealPressedTimes==2:
            self.deckN += 1  # 가려진 카드
            self.cardsphotoimage[self.deckN] = Card(self.cardDeck[self.deckN])
            self.dealer.addCard(self.cardsphotoimage[self.deckN].getValue(),
                                self.cardsphotoimage[self.deckN].filename())
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
        for i in range(5):
            p = PhotoImage(file='GodoriCards/' + self.dealer.cards[i][1])
            self.LcardsDealer[i].configure(image=p)  # 이미지 레퍼런스 변경
            self.LcardsDealer[i].image = p  # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
            self.LScoresDealer[i].configure(text=self.dealer.cards[i][0])
        self.CheckWinner()
        #딜러점수 라벨에 보여야함여

    def PressedAgain(self):
        self.cardDeck.clear()
        self.deckN = 0
        self.pstatevalue = 0
        self.dstatevalue = 0
        self.DealPressedTimes=0
        self.betMoney1=0
        self.betMoney2=0
        self.betMoney3=0

        self.playerFlag1 = 0
        self.playerFlag2 = 0
        self.playerFlag3 = 0
        self.playerFlagD = 0

        self.StartButtonState()
        self.Lplayer1State.configure(text="")
        self.Lplayer2State.configure(text="")
        self.Lplayer3State.configure(text="")
        self.LdealerState.configure(text="")
        self.Lplayer1StateJB.configure(text="")
        self.Lplayer2StateJB.configure(text="")
        self.Lplayer3StateJB.configure(text="")
        self.LdealerStateJB.configure(text="")

        self.LUser1_betMoney.configure(text="0만")
        self.LUser2_betMoney.configure(text="0만")
        self.LUser3_betMoney.configure(text="0만")

        self.resultLabel1.configure(text="")
        self.resultLabel2.configure(text="")
        self.resultLabel3.configure(text="")

        del self.player1
        del self.player2
        del self.player3
        del self.dealer

        for i in range(5):
            self.LcardsPlayer1[i].configure(image='')
            self.LcardsPlayer2[i].configure(image='')
            self.LcardsPlayer3[i].configure(image='')
            self.LcardsDealer[i].configure(image='')
            self.LScoresPlayer1[i].configure(text="",fg="white")
            self.LScoresPlayer2[i].configure(text="",fg="white")
            self.LScoresPlayer3[i].configure(text="",fg="white")
            self.LScoresDealer[i].configure(text="",fg="white")

        self.LcardsPlayer1.clear()
        self.LcardsPlayer2.clear()
        self.LcardsPlayer3.clear()
        self.LcardsDealer.clear()

    def CheckWinner(self):
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

        self.Player1Check()
        self.Player2Check()
        self.Player3Check()
        self.DealerCheck()

        self.JokboCheck(self.toJokbo1,self.toJokbo2,self.toJokbo3,self.toJokboD)
#
        # if self.pCheck > self.dCheck:
        #     #PlaySound('Resources/sounds/win.wav', SND_FILENAME)
        #     self.Lstatus.configure(text="Win")
        #     self.playerMoney += self.betMoney
        #
        # elif self.pCheck == self.dCheck:
        #     if self.pstatevalue > self.dstatevalue:
        #         self.Lstatus.configure(text="Win")
        #         #PlaySound('Resources/sounds/win.wav', SND_FILENAME)
        #     elif self.pstatevalue == self.dstatevalue:
        #         self.Lstatus.configure(text="Push")
        #     else:
        #         self.Lstatus.configure(text="Lose")
        #         #PlaySound('Resources/sounds/wrong.wav', SND_FILENAME)
        #     self.playerMoney = self.playerMoney
        #
        # else:
        #     #PlaySound('Resources/sounds/wrong.wav', SND_FILENAME)
        #     self.Lstatus.configure(text="Lose")
        #     self.playerMoney -= self.betMoney
        #
        # self.LUserMoney.configure(text= str(self.playerMoney))
        # self.betMoney = 10
        # self.LUser1_betMoney.configure(text="$" + str(self.betMoney))

    def Player1Check(self):  # 플레이어의 상태를 체크 한 당
        p1val=[0 for _ in range(5)]
        self.toJokbo1=[] #메이드 3개 빼놓을 리스트
        idx=0
        idx2=0
        idx3=0
        key=0
        check=True

        for i in range(5):
            p1val[i] = self.player1.cards[i][0]  # 점수 각각 저장
        for i in range(21):
            if self.cardtable[i][0] in p1val[:]:  # 찾아서 있으면
                idx = p1val.index(self.cardtable[i][0])  # 체크할 인덱스를 p1val 인덱스로 바꿈
                key = i  # 족보 인덱스
                if self.cardtable[key][1] in p1val[:]:  # key 족보 두번째 요소 찾기
                    if p1val.index(self.cardtable[key][1]) != idx:
                        idx2 = p1val.index(self.cardtable[i][1])
                        if self.cardtable[key][2] in p1val[:]:
                            if p1val.index(self.cardtable[key][2])!=idx2 and p1val.index(self.cardtable[key][2])!=idx:
                                idx3 = p1val.index(self.cardtable[i][2])
                                for j in range(5):
                                    if j != idx and j != idx2 and j != idx3:
                                        self.toJokbo1.append(p1val[j])
                                self.LScoresPlayer1[idx].configure(fg="yellow")
                                self.LScoresPlayer1[idx2].configure(fg="yellow")
                                self.LScoresPlayer1[idx3].configure(fg="yellow")
                                self.Lplayer1State.configure(text=str(self.cardtable[i][3]))
                                self.playerFlag1 = 1
                                return 1
        self.toJokbo1.append(0)
        self.Lplayer1State.configure(text="노메이드")

    def Player2Check(self):
        p2val = [0 for _ in range(5)]
        self.toJokbo2 = []  # 메이드 3개 빼놓을 리스트
        idx = 0
        key = 0
        idx2=0
        idx3=0
        check=True

        for i in range(5):
            p2val[i] = self.player2.cards[i][0]  # 점수 각각 저장

        for i in range(21):
            if self.cardtable[i][0] in p2val[:]:  # 찾아서 있으면
                idx = p2val.index(self.cardtable[i][0])  # 체크할 인덱스를 p1val 인덱스로 바꿈
                key = i  # 족보 인덱스
                if self.cardtable[key][1] in p2val[:]:  # key 족보 두번째 요소 찾기
                    if p2val.index(self.cardtable[key][1]) != idx:
                        idx2 = p2val.index(self.cardtable[i][1])
                        if self.cardtable[key][2] in p2val[:]:
                            if p2val.index(self.cardtable[key][2]) != idx2 and p2val.index(
                                    self.cardtable[key][2]) != idx:
                                idx3 = p2val.index(self.cardtable[i][2])
                                for j in range(5):
                                    if j != idx and j != idx2 and j != idx3:
                                        self.toJokbo2.append(p2val[j])
                                self.LScoresPlayer2[idx].configure(fg="yellow")
                                self.LScoresPlayer2[idx2].configure(fg="yellow")
                                self.LScoresPlayer2[idx3].configure(fg="yellow")
                                self.Lplayer2State.configure(text=str(self.cardtable[i][3]))
                                self.playerFlag2 = 1
                                return 1
        self.toJokbo2.append(0)
        self.Lplayer2State.configure(text="노메이드")


    def Player3Check(self):
        p3val = [0 for _ in range(5)]
        self.toJokbo3 = []  # 메이드 3개 빼놓을 리스트
        idx = 0
        idx2=0
        idx3=0
        key = 0
        check=True

        for i in range(5):
            p3val[i] = self.player3.cards[i][0]  # 점수 각각 저장
        for i in range(21):
            if self.cardtable[i][0] in p3val[:]:  # 찾아서 있으면
                idx = p3val.index(self.cardtable[i][0])  # 체크할 인덱스를 p1val 인덱스로 바꿈
                key = i  # 족보 인덱스
                if self.cardtable[key][1] in p3val[:]:  # key 족보 두번째 요소 찾기
                    if p3val.index(self.cardtable[key][1]) != idx:
                        idx2 = p3val.index(self.cardtable[i][1])
                        if self.cardtable[key][2] in p3val[:]:
                            if p3val.index(self.cardtable[key][2]) != idx2 and p3val.index(
                                    self.cardtable[key][2]) != idx:
                                idx3 = p3val.index(self.cardtable[i][2])
                                for j in range(5):
                                    if j != idx and j != idx2 and j != idx3:
                                        self.toJokbo3.append(p3val[j])
                                self.LScoresPlayer3[idx].configure(fg="yellow")
                                self.LScoresPlayer3[idx2].configure(fg="yellow")
                                self.LScoresPlayer3[idx3].configure(fg="yellow")
                                self.Lplayer3State.configure(text=str(self.cardtable[i][3]))
                                self.playerFlag3 = 1
                                return 1
        self.toJokbo3.append(0)
        self.Lplayer3State.configure(text="노메이드")

    def DealerCheck(self):
        dval = [0 for _ in range(5)]
        self.toJokboD = []  # 메이드 3개 빼놓을 리스트
        idx = 0
        idx2 = 0
        idx3 = 0
        key = 0

        for i in range(5):
            dval[i] = self.dealer.cards[i][0]  # 점수 각각 저장

        for i in range(21):
            if self.cardtable[i][0] in dval[:]:  # 찾아서 있으면
                idx = dval.index(self.cardtable[i][0])  # 체크할 인덱스를 p1val 인덱스로 바꿈
                key = i  # 족보 인덱스
                if self.cardtable[key][1] in dval[:]:  # key 족보 두번째 요소 찾기
                    if dval.index(self.cardtable[key][1]) != idx:
                        idx2 = dval.index(self.cardtable[i][1])
                        if self.cardtable[key][2] in dval[:]:
                            if dval.index(self.cardtable[key][2]) != idx2 and dval.index(
                                    self.cardtable[key][2]) != idx:
                                idx3 = dval.index(self.cardtable[i][2])
                                for j in range(5):
                                    if j != idx and j != idx2 and j != idx3:
                                        self.toJokboD.append(dval[j])
                                self.LdealerState.configure(text=str(self.cardtable[i][3]))
                                self.LScoresDealer[idx].configure(fg="yellow")
                                self.LScoresDealer[idx2].configure(fg="yellow")
                                self.LScoresDealer[idx3].configure(fg="yellow")
                                self.playerFlagD = 1
                                return 1

        self.toJokboD.append(0)
        self.LdealerState.configure(text="노메이드")

    def JokboCheck(self,lst1,lst2,lst3,lstD):

        #         # 1순위 - 2장 self.value가 3,8 >> 38광땡
        #         # 2순위 - self.value가 1,3 또는 1,8 >> 광땡
        #         # 3순위 - self.value가 같을 때 >> 땡 (월이 높을 수록 높은 족보)
        #         # 4순위 - 1,2,3 순위 해당x 두 패의 숫자 합이 1~8 >> 끗
        #         # 5순위 - 2,8월 또는 3,7월 끗 수가 0 >> 가장낮음>> 망통

        numCheck1 = 0
        numCheck2 = 0
        numCheck3 = 0
        numCheckD = 0
        countRank1=0
        countRank2 = 0
        countRank3 = 0
        countRankD = 0

        print(lst1,lst2,lst3,lstD)

        if self.playerFlagD == 1:
            if self.playerFlag1 == 0:
                self.resultLabel1.configure(text="패")
            if self.playerFlag2 == 0:
                self.resultLabel2.configure(text="패")
            if self.playerFlag3 == 0:
                self.resultLabel3.configure(text="패")

        #리스트 1이 들어왔는지 확인
        if len(lst1)==2:
            if lst1 == [3, 8]:
                self.Lplayer1StateJB.configure(text="38광땡")
                countRank1 = 5
            if lst1 == [1, 3] or lst1 == [1, 8]:
                self.Lplayer1StateJB.configure(text=str(lst1[0]) + str(lst1[1]) + "광땡")
                countRank1 = 4
            if lst1[0] == lst1[1]:
                self.Lplayer1StateJB.configure(text=str(lst1[0]) + "땡")
                countRank1 = 3
                numCheck1 = lst1[0]
            if 1<= lst1[0] + lst1[1] <= 9 and lst1[0] != lst1[1]:
                self.Lplayer1StateJB.configure(text=str(lst1[0] + lst1[1]) + "끗")
                countRank1 = 2
                numCheck1 = lst1[0] + lst1[1]
            if (lst1[0] == 2 and lst1[1] == 8) or (lst1[0] == 3 and lst1[1] == 7):
                self.Lplayer1StateJB.configure(text="망통")
                countRank1 = 1
            if (10 <= lst1[0] + lst1[1]) and lst1[0] == lst1[1]:
                self.Lplayer1StateJB.configure(text=str(lst1[0]) + "땡")
                numCheck1 = lst1[0]
            if 10 <= lst1[0] + lst1[1] and lst1[0] != lst1[1]:
                self.Lplayer1StateJB.configure(text=str(lst1[0] + lst1[1] - 10) + "끗")
                countRank1 = 2
                numCheck1 = lst1[0] + lst1[1] - 10

        if len(lst2) == 2:
            if lst2== [3, 8]:
                self.Lplayer2StateJB.configure(text="38광땡")
                countRank2 = 5
            if lst2 == [1, 3] or lst2 == [1, 8]:
                self.Lplayer2StateJB.configure(text=str(lst2[0]) + str(lst2[1]) + "광땡")
                countRank2 = 4
            if lst2[0] == lst2[1]:
                self.Lplayer2StateJB.configure(text=str(lst2[0]) + "땡")
                countRank2 = 3
                numCheck2 = lst2[0]
            if 1 <= lst2[0] + lst2[1]<= 9 and lst2[0] != lst2[1]:
                self.Lplayer2StateJB.configure(text=str(lst2[0] + lst2[1]) + "끗")
                countRank2 = 2
                numCheck2 = lst2[0] + lst2[1]
            if (lst2[0] == 2 and lst2[1] == 8) or (lst2[0] == 3 and lst2[1] == 7):
                self.Lplayer2StateJB.configure(text="망통")
                countRank2 = 1
            if (10 <= lst2[0] + lst2[1]) and lst2[0] == lst2[1]:
                self.Lplayer2StateJB.configure(text=str(lst2[0]) + "땡")
                numCheck2 = lst2[0]
            if 10 <= lst2[0] + lst2[1] and lst2[0] != lst2[1]:
                self.Lplayer2StateJB.configure(text=str(lst2[0] + lst2[1] - 10) + "끗")
                countRank2 = 2
                numCheck2 = lst2[0] + lst2[1] - 10

        if len(lst3) == 2:
            if lst3== [3, 8]:
                self.Lplayer3StateJB.configure(text="38광땡")
                countRank3 = 5
            if lst3 == [1, 3] or lst3 == [1, 8]:
                self.Lplayer3StateJB.configure(text=str(lst3[0]) + str(lst3[1]) + "광땡")
                countRank3 = 4
            if lst3[0] == lst3[1]:
                self.Lplayer3StateJB.configure(text=str(lst3[0]) + "땡")
                countRank3 = 3
                numCheck3 = lst3[0]
            if 1 <= lst3[0] + lst3[1]<= 9 and lst3[0] != lst3[1]:
                self.Lplayer3StateJB.configure(text=str(lst3[0] + lst3[1]) + "끗")
                countRank3 = 2
                numCheck3 = lst3[0] + lst3[1]
            if (lst3[0] == 2 and lst3[1] == 8) or (lst3[0] == 3 and lst3[1] == 7):
                self.Lplayer3StateJB.configure(text="망통")
                countRank3 = 1
            if (10 <= lst3[0] + lst3[1]) and lst3[0] == lst3[1]:
                self.Lplayer3StateJB.configure(text=str(lst3[0]) + "땡")
                numCheck3 = lst3[0]
            if 10 <= lst3[0] + lst3[1] and lst3[0] != lst3[1]:
                self.Lplayer3StateJB.configure(text=str(lst3[0] + lst3[1] - 10) + "끗")
                countRank3 = 2
                numCheck3 = lst3[0] + lst3[1] - 10

        if len(lstD) == 2:
            if lstD== [3, 8]:
                self.LdealerStateJB.configure(text="38광땡")
                countRankD = 5
            if lstD == [1, 3] or lstD == [1, 8]:
                self.LdealerStateJB.configure(text=str(lstD[0]) + str(lstD[1]) + "광땡")
                countRankD = 4
            if lstD[0] == lstD[1]:
                self.LdealerStateJB.configure(text=str(lstD[0]) + "땡")
                countRankD = 3
                numCheckD = lstD[0]
            if 1 <= lstD[0] + lstD[1]<= 9 and lstD[0] != lstD[1]:
                self.LdealerStateJB.configure(text=str(lstD[0] + lstD[1]) + "끗")
                countRankD = 2
                numCheckD = lstD[0] + lstD[1]
            if (lstD[0] == 2 and lstD[1] == 8) or (lstD[0] == 3 and lstD[1] == 7):
                self.LdealerStateJB.configure(text="망통")
                countRankD = 1
            if (10 <= lstD[0] + lstD[1]) and lstD[0] == lstD[1]:
                self.LdealerStateJB.configure(text=str(lstD[0]) + "땡")
                numCheckD = lstD[0]
            if 10 <= lstD[0] + lstD[1] and lstD[0] != lstD[1]:
                self.LdealerStateJB.configure(text=str(lstD[0] + lstD[1] - 10) + "끗")
                countRankD = 2
                numCheckD = lstD[0] + lstD[1] - 10

        # self.betMoney2 += 1
        # self.playerMoney -= 1
        # self.LUser2_betMoney.configure(text=str(self.betMoney2) + "만")
        # self.LUserMoney.configure(text=str(self.playerMoney) + "만")
        print("넘체크들!:",numCheck1,numCheck2,numCheck3,numCheckD)
        if countRank1 != 0:
            if countRank1 < countRankD:
                self.resultLabel1.configure(text="패")
            elif countRank1 == countRankD:
                if numCheck1 < numCheckD:
                    self.resultLabel1.configure(text="패")
                elif numCheck1 > numCheckD:
                    self.resultLabel1.configure(text="승")
                    self.playerMoney += self.betMoney1 * 2
                    self.LUserMoney.configure(text=str(self.playerMoney) + "만")
                elif numCheck1==numCheckD:
                    self.playerMoney += self.betMoney1
                    self.LUserMoney.configure(text=str(self.playerMoney) + "만")
            elif countRank1 > countRankD:
                self.resultLabel1.configure(text="승")
                self.playerMoney += self.betMoney1 * 2
                self.LUserMoney.configure(text=str(self.playerMoney) + "만")

        if countRank2 != 0:
            if countRank2 < countRankD:
                self.resultLabel2.configure(text="패")
            elif countRank2 == countRankD:
                if numCheck2 < numCheckD:
                    self.resultLabel2.configure(text="패")
                elif numCheck2 > numCheckD:
                    self.resultLabel2.configure(text="승")
                    self.playerMoney += self.betMoney2 * 2
                    self.LUserMoney.configure(text=str(self.playerMoney) + "만")
                elif numCheck2==numCheckD:
                    self.playerMoney += self.betMoney2
                    self.LUserMoney.configure(text=str(self.playerMoney) + "만")
            elif countRank2 > countRankD:
                self.resultLabel2.configure(text="승")
                self.playerMoney += self.betMoney2 * 2
                self.LUserMoney.configure(text=str(self.playerMoney) + "만")

        if countRank3 != 0:
            if countRank3 < countRankD:
                self.resultLabel3.configure(text="패")
            elif countRank3 == countRankD:
                if numCheck3 < numCheckD:
                    self.resultLabel3.configure(text="패")
                elif numCheck3 > numCheckD:
                    self.resultLabel3.configure(text="승")
                    self.playerMoney += self.betMoney3 * 2
                    self.LUserMoney.configure(text=str(self.playerMoney) + "만")
                elif numCheck3==numCheckD:
                    self.playerMoney += self.betMoney3
                    self.LUserMoney.configure(text=str(self.playerMoney) + "만")
            elif countRank3 > countRankD:
                self.resultLabel3.configure(text="승")
                self.playerMoney += self.betMoney3 * 2
                self.LUserMoney.configure(text=str(self.playerMoney) + "만")

    def inputCardList(self):
        n = 0
        for i in range(10, 101, 10):
            for j in range(1, 5):
                self.cardDeck[n] = i+j
                n += 1

DorijitGo()