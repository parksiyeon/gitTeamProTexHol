from CCard import *
class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.chars=[]
        self.N = 0

    def inHand(self):
        return self.N

    def addCard(self,c,f):
        self.cards.append([c,f])
        self.N += 1
        return c

    def reset(self):
        self.cards.clear()
        self.N=0

