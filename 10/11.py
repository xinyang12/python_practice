from random import randint


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def Value(self):
        if self.rank >= 10:
            return 10
        else:
            return self.rank

    def __str__(self):
        if self.suit == 'd':
            suit_name = '方块'
        elif self.suit == 'c':
            suit_name = '草花'
        elif self.suit == 'h':
            suit_name = '红心'
        else:
            suit_name = '黑桃'

        if self.rank == 1:
            rank_name = 'A'
        elif self.rank == 11:
            rank_name = 'J'
        elif self.rank == 12:
            rank_name = 'Q'
        elif self.rank == 13:
            rank_name = 'K'
        else:
            rank_name = str(self.rank)

        return suit_name + rank_name + "，对应的21点值是:" + str(self.Value())


def main():
    n = int(input("随机生成多少张纸牌呢: "))
    for i in range(n):
        suit = generateSuit(randint(1, 4))
        rank = randint(1, 13)
        card = Card(rank, suit)
        print(card)


def generateSuit(n):
    if n == 1:
        return 'd'
    elif n == 2:
        return 'c'
    elif n == 3:
        return 'h'
    else:
        return 's'


if __name__ == "__main__":
    main()
