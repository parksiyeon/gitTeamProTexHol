from tkinter import *
from tkinter import font
from winsound import *
from Card import *
from Player import *
import random


class TexasHoldem:
    def __init__(self):
        self.window = Tk()
        self.window.title("Texas Holdem")
        self.window.geometry("800x600")
        self.window.configure(bg="green")

        self.bg = PhotoImage(file='Resources/cards/table.gif')
        self.gamebg = Label(image=self.bg)
        self.gamebg.place(x=0, y=0)
        self.fontstyle = font.Font(self.window, size=24, weight='bold', family='Consolas')
        self.fontstyle2 = font.Font(self.window, size=16, weight='bold', family='Consolas')
        self.setupButton()
        self.setupLabel()
        self.betMoney = 10
        self.playerMoney = 2500
        self.GetPmoney = 2500
        self.LcardsPlayer = []  # 플레이어가 뽑은 카드의 라벨 리스트
        self.LcardsDealer = []  # 딜러가 뽑은 카드의 라벨 리스트
        self.LcardsCommon = []
        self.deckN = 0
        self.commoncardsN = 0
        self.cardsphotoimage = [0 for _ in range(10)]
        self.pstatevalue = 0
        self.dstatevalue = 0
        self.pCheck = 0
        self.dCheck = 0
        self.window.mainloop()

    def setupButton(self):
        self.Check = Button(self.window, text="Check", width=6, height=1, font=self.fontstyle2,
                            command=self.pressedCheck)
        self.Check.place(x=50, y=500)
        self.Bx1 = Button(self.window, text="Bx1", width=6, height=1, font=self.fontstyle2, command=self.pressedBx1)
        self.Bx1.place(x=150, y=500)
        self.Bx2 = Button(self.window, text="Bx2", width=6, height=1, font=self.fontstyle2, command=self.pressedBx2)
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
        self.LbetMoney = Label(text="$10", width=4, height=1, font=self.fontstyle, bg="green", fg="orange")
        self.LbetMoney.place(x=200, y=450)
        self.LplayerMoney = Label(text="You have $2500", width=15, height=1, font=self.fontstyle, bg="green",
                                  fg="orange")
        self.LplayerMoney.place(x=500, y=450)
        self.LplayerState = Label(text="", width=12, height=1, font=self.fontstyle2, bg="green", fg="white")
        self.LplayerState.place(x=300, y=350)
        self.LdealerState = Label(text="", width=12, height=1, font=self.fontstyle2, bg="green", fg="white")
        self.LdealerState.place(x=300, y=100)
        self.Lstatus = Label(text="", width=12, height=1, font=self.fontstyle, bg="green", fg="red")
        self.Lstatus.place(x=550, y=350)

    def pressedCheck(self):
        self.opendealercard()

    def pressedBx1(self):
        self.betMoney += self.betMoney
        self.playerMoney = self.GetPmoney - self.betMoney
        self.LbetMoney.configure(text="$" + str(self.betMoney))
        self.LplayerMoney.configure(text="You have $" + str(self.playerMoney))
        self.Deal['state'] = 'active'
        self.Deal['bg'] = 'SystemButtonFace'
        PlaySound('Resources/sounds/chip.wav', SND_FILENAME)

    def pressedBx2(self):
        self.betMoney += self.betMoney * 2
        self.playerMoney = self.GetPmoney - self.betMoney
        self.LbetMoney.configure(text="$" + str(self.betMoney))
        self.LplayerMoney.configure(text="You have $" + str(self.playerMoney))
        self.Deal['state'] = 'active'
        self.Deal['bg'] = 'SystemButtonFace'
        PlaySound('Resources/sounds/chip.wav', SND_FILENAME)

    def deal(self):  # 딜 처음 시작 때 불리는 세팅 함수
        self.player = Player("player")
        self.dealer = Player("dealer")
        self.common = Player("Common")
        self.cardsphotoimage = [0 for _ in range(10)]
        # 카드 덱 52장 셔플링 0,1,,.51
        self.cardDeck = [i for i in range(52)]
        random.shuffle(self.cardDeck)

    def hitDealer(self):
        self.deckN += 1  # 가려진 카드
        self.cardsphotoimage[self.deckN] = Card(self.cardDeck[self.deckN])
        self.dealer.addCard(self.cardsphotoimage[self.deckN].getValue(), self.cardsphotoimage[self.deckN].filename(),
                            self.cardsphotoimage[self.deckN].seperatename())
        p1 = PhotoImage(file='Resources/cards/b2fv.png')  # 카드 가려줄 뒷면 이미지! 추후 지워짐(리스트에 추가할필요 없음)
        self.LcardsDealer.append(Label(self.window, image=p1, bd=0, bg='green'))
        self.LcardsDealer[self.dealer.inHand() - 1].image = p1
        self.LcardsDealer[self.dealer.inHand() - 1].place(x=100, y=100)

        self.deckN += 1
        self.cardsphotoimage[self.deckN] = Card(self.cardDeck[self.deckN])
        self.dealer.addCard(self.cardsphotoimage[self.deckN].getValue(), self.cardsphotoimage[self.deckN].filename(),
                            self.cardsphotoimage[self.deckN].seperatename())
        p = PhotoImage(file='Resources/cards/b2fv.png')
        self.LcardsDealer.append(Label(self.window, image=p, bd=0, bg='green'))
        self.LcardsDealer[self.dealer.inHand() - 1].image = p
        self.LcardsDealer[self.dealer.inHand() - 1].place(x=180, y=100)

    def SetButtons(self):
        self.Check['state'] = 'active'
        self.Check['bg'] = 'SystemButtonFace'
        self.Bx1['state'] = 'active'
        self.Bx1['bg'] = 'SystemButtonFace'
        self.Bx2['state'] = 'active'
        self.Bx2['bg'] = 'SystemButtonFace'

        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'

    def pressedDeal(self):
        if self.deckN <= 1:
            self.SetButtons()
            self.deal()
            self.cardsphotoimage[self.deckN] = Card(self.cardDeck[self.deckN])  # 카드 덱에 저장되어있는 0부터 52까지의 랜덤 숫자를 넘김
            self.player.addCard(self.cardsphotoimage[self.deckN].getValue(),
                                self.cardsphotoimage[self.deckN].filename(),
                                self.cardsphotoimage[self.deckN].seperatename())
            p = PhotoImage(file='Resources/cards/' + self.player.cards[self.deckN][1])
            self.LcardsPlayer.append(Label(self.window, image=p, bd=0, bg='green'))
            self.LcardsPlayer[self.player.inHand() - 1].image = p
            self.LcardsPlayer[self.player.inHand() - 1].place(x=100, y=350)

            self.deckN += 1
            self.cardsphotoimage[self.deckN] = Card(self.cardDeck[self.deckN])
            self.player.addCard(self.cardsphotoimage[self.deckN].getValue(),
                                self.cardsphotoimage[self.deckN].filename(),
                                self.cardsphotoimage[self.deckN].seperatename())
            p1 = PhotoImage(file='Resources/cards/' + self.player.cards[self.deckN][1])
            self.LcardsPlayer.append(Label(self.window, image=p1, bd=0, bg='green'))
            self.LcardsPlayer[self.player.inHand() - 1].image = p1
            self.LcardsPlayer[self.player.inHand() - 1].place(x=180, y=350)
            self.hitDealer()

        elif self.deckN >= 3:
            self.deckN += 1
            self.DealCommonCards()

    def DealCommonCards(self):
        if self.deckN == 4:
            for j in range(self.deckN, 7, 1):
                self.cardsphotoimage[j] = Card(self.cardDeck[j])  # 카드 덱에 저장되어있는 0부터 52까지의 랜덤 숫자를 넘김
                self.common.addCard(self.cardsphotoimage[j].getValue(), self.cardsphotoimage[j].filename(),
                                    self.cardsphotoimage[j].seperatename())
                p = PhotoImage(file='Resources/cards/' + self.common.cards[self.commoncardsN][1])
                self.LcardsCommon.append(Label(self.window, image=p, bd=0, bg='green'))
                self.LcardsCommon[self.common.inHand() - 1].image = p
                self.LcardsCommon[self.common.inHand() - 1].place(x=200 + (self.commoncardsN) * 80, y=225)
                self.commoncardsN += 1
                self.deckN += 1

        elif self.deckN >= 7:
            self.cardsphotoimage[self.deckN] = Card(self.cardDeck[self.deckN])  # 카드 덱에 저장되어있는 0부터 52까지의 랜덤 숫자를 넘김
            self.common.addCard(self.cardsphotoimage[self.deckN].getValue(),
                                self.cardsphotoimage[self.deckN].filename(),
                                self.cardsphotoimage[self.deckN].seperatename())
            p = PhotoImage(file='Resources/cards/' + self.common.cards[self.commoncardsN][1])
            self.LcardsCommon.append(Label(self.window, image=p, bd=0, bg='green'))
            self.LcardsCommon[self.common.inHand() - 1].image = p
            self.LcardsCommon[self.common.inHand() - 1].place(x=200 + (self.commoncardsN) * 80, y=225)
            self.commoncardsN += 1

    def opendealercard(self):
        for i in range(2):
            p = PhotoImage(file="Resources/cards/" + self.dealer.cards[i][1])
            self.LcardsDealer[i].configure(image=p)  # 이미지 레퍼런스 변경
            self.LcardsDealer[i].image = p  # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
            self.LdealerState.configure(text=str(self.dealer.value()))
        self.CheckWinner()

    def pressedAgain(self):
        self.cardDeck.clear()
        self.deckN = 0
        self.commoncardsN = 0
        self.pstatevalue = 0
        self.dstatevalue = 0
        self.GetPmoney = self.playerMoney

        self.setupButton()
        self.LplayerState.configure(text="")
        self.LdealerState.configure(text="")
        self.Lstatus.configure(text="")
        self.Lstatus.configure(text="")

        del self.player
        del self.dealer
        del self.common

        for i in range(2):
            self.LcardsPlayer[i].configure(image='')
            self.LcardsDealer[i].configure(image='')
        for i in range(5):
            self.LcardsCommon[i].configure(image='')

        self.LcardsPlayer.clear()
        self.LcardsDealer.clear()
        self.LcardsCommon.clear()

    def CheckWinner(self):
        self.LplayerMoney.configure(text="You have $" + str(self.playerMoney))
        self.Check['state'] = 'disabled'
        self.Check['bg'] = 'gray'
        self.Bx1['state'] = 'disabled'
        self.Bx1['bg'] = 'gray'
        self.Bx2['state'] = 'disabled'
        self.Bx2['bg'] = 'gray'
        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'active'
        self.Again['bg'] = 'SystemButtonFace'

        self.pCheck = self.PlayerCheck()
        self.dCheck = self.DealerCheck()

        if self.pCheck > self.dCheck:
            PlaySound('Resources/sounds/win.wav', SND_FILENAME)
            self.Lstatus.configure(text="Win")
            self.playerMoney += self.betMoney

        elif self.pCheck == self.dCheck:
            if self.pstatevalue > self.dstatevalue:
                self.Lstatus.configure(text="Win")
                PlaySound('Resources/sounds/win.wav', SND_FILENAME)
            elif self.pstatevalue == self.dstatevalue:
                self.Lstatus.configure(text="Push")
            else:
                self.Lstatus.configure(text="Lose")
                PlaySound('Resources/sounds/wrong.wav', SND_FILENAME)
            self.playerMoney = self.playerMoney

        else:
            PlaySound('Resources/sounds/wrong.wav', SND_FILENAME)
            self.Lstatus.configure(text="Lose")
            self.playerMoney -= self.betMoney

        self.LplayerMoney.configure(text="You have $" + str(self.playerMoney))
        self.betMoney = 10
        self.LbetMoney.configure(text="$" + str(self.betMoney))

    def PlayerCheck(self):  # 플레이어의 상태를 체크 한 당
        hc = 0
        sc = 0
        cc = 0
        dc = 0
        tmp1 = False
        tmp2 = False
        exceptint = 0
        lst = []
        self.player.cards.extend(self.common.cards)

        for i in range(7):
            lst.append(self.player.cards[i][0])

        for i in range(14):
            if lst.count(i) == 3:
                tmp1 = True
                self.pstatevalue = i
            elif lst.count(i) == 2:
                tmp2 = True

        if tmp1 == tmp2 == True:
            self.LplayerState.configure(text="Full House" + str(self.pstatevalue))
            tmp1 = False
            tmp2 = False

            return 6

        for i in range(len(self.player.cards)):
            if self.player.cards[i][2] == 'Hearts':
                hc += 1
            elif self.player.cards[i][2] == 'Spades':
                sc += 1
            elif self.player.cards[i][2] == 'Clubs':
                cc += 1
            elif self.player.cards[i][2] == 'Diamonds':
                dc += 1

        if hc >= 5 or sc >= 5 or cc >= 5 or dc >= 5:
            self.LplayerState.configure(text="Flush" + str(self.pstatevalue))
            return 5

        lst.sort()
        for i in range(2):
            if lst[i + 4] - lst[i + 3] == lst[i + 3] - lst[i + 2] == lst[i + 2] - lst[i + 1] == lst[i + 1] - lst[
                i] == 1:
                self.pstatevalue = lst[i]
                self.LplayerState.configure(text="Straight" + str(self.pstatevalue))
                return 4

        for i in range(14):
            if lst.count(i) >= 3:
                self.pstatevalue = i
                self.LplayerState.configure(text="Triple" + str(self.pstatevalue))
                return 3

        for i in range(14):
            if tmp1 == False and lst.count(i) == 2:
                self.pstatevalue = i
                exceptint = i

        for i in range(14):
            if i != exceptint and lst.count(i) == 2:
                self.LplayerState.configure(text="Two Pair" + str(self.pstatevalue))
                return 2

        for i in range(14):
            if lst.count(i) == 2:
                self.pstatevalue = i
                self.LplayerState.configure(text="One Pair" + str(self.pstatevalue))
                return 1

        self.pstatevalue = max(lst)
        self.LplayerState.configure(text="No Pair" + str(self.pstatevalue))
        return 0

    def DealerCheck(self):
        hc = 0
        sc = 0
        cc = 0
        dc = 0
        tmp1 = False
        tmp2 = False
        exceptint = 0
        lst = []
        self.dealer.cards.extend(self.common.cards)

        for i in range(7):
            lst.append(self.dealer.cards[i][0])

        for i in range(14):
            if lst.count(i) == 3:
                tmp1 = True
                self.dstatevalue = i
            elif lst.count(i) == 2:
                tmp2 = True

        if tmp1 == tmp2 == True:
            self.LdealerState.configure(text="Full House" + str(self.dstatevalue))
            return 6

        for i in range(len(self.dealer.cards)):
            if self.dealer.cards[i][2] == 'Hearts':
                hc += 1
            elif self.dealer.cards[i][2] == 'Spades':
                sc += 1
            elif self.dealer.cards[i][2] == 'Clubs':
                cc += 1
            elif self.dealer.cards[i][2] == 'Diamonds':  # dia
                dc += 1

        if hc >= 5 or sc >= 5 or cc >= 5 or dc >= 5:
            self.LdealerState.configure(text="Flush" + str(self.dstatevalue))
            return 5

        lst.sort()
        for i in range(2):
            if lst[i + 4] - lst[i + 3] == lst[i + 3] - lst[i + 2] == lst[i + 2] - lst[i + 1] == lst[i + 1] - lst[
                i] == 1:
                self.dstatevalue = lst[i]
                self.LdealerState.configure(text="Straight" + str(self.dstatevalue))
                return 4

        for i in range(14):
            if lst.count(i) == 3:
                self.dstatevalue = i
                self.LdealerState.configure(text="Triple" + str(self.dstatevalue))
                return 3

        for i in range(14):
            if tmp1 == False and lst.count(i) == 2:
                self.dstatevalue = i
                exceptint = i

        for i in range(14):
            if i != exceptint and lst.count(i) == 2:
                self.LdealerState.configure(text="Two Pair" + str(self.dstatevalue))
                return 2

        self.dstatevalue = 0

        for i in range(14):
            if lst.count(i) == 2:
                self.dstatevalue = i
                self.LdealerState.configure(text="One Pair" + str(self.dstatevalue))
                return 1
        self.dstatevalue = max(lst)
        self.LdealerState.configure(text="No Pair" + str(self.dstatevalue))
        return 0


TexasHoldem()