class Card:
    def __init__(self, temp):  # 카드 랜덤 넘버
        self.value = temp // 10  # 1..10 ( 0월까지 씀)
        self.suit = temp % 10 # n월의 화투 피? 번호

    def getsuit(self):  # n월
        return self.suit

    def getValue(self): # 끗 또는 땡 처리할 때
        return self.value

    def filename(self):  # 화투패 이미지
        return str(self.getValue()) +"."+str(self.getsuit()) + ".gif"
