class Card:
    def __init__(self, temp):  # 렌덤 넘버0..51 값을 입력받아서 카드 객체 생성
        self.value = temp % 12 + 1  # 1..13
        self.suit = temp %4+1

    def getsuit(self):  # 카드 무늬 결정
        return self.suit

    def getValue(self):  # 카드 값 JQK는 10으로 결정
        return self.value

    def seperatename(self):
        return self.getsuit()

    def filename(self):  # 카드 이미지 파일 이름
        return str(self.getValue()) +"."+str(self.getsuit()) + ".gif"
