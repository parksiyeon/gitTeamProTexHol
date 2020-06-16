from CCard import *
class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.chars=[]
        self.N = 0

    def inHand(self):
        return self.N

    def addCard(self,c,f,n):
        self.cards.append([c,f,n])
        self.N += 1
        return c

    def reset(self):
        self.cards.clear()
        self.N=0

#ace는 1혹은 11로 모두 사용 가능
#일단 11로 계산한 후 21이 넘어가면 1로 정정