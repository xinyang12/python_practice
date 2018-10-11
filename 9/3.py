import random


def print_intro():
    print("这个程序模拟排球比赛")


def get_inputs():
    a = float(input("输入A队获胜的概率: "))
    b = float(input("输入B队获胜的概率: "))
    n = int(input("输入模拟的次数: "))
    return a, b, n


def simNGames(a, b, n):
    winA = winB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(a, b)
        if scoreA > scoreB:
            winA += 1
        else:
            winB += 1

    return winA, winB


def simOneGame(a, b):
    scoreA = scoreB = 0
    start = 'A'
    while not game_over(scoreA, scoreB):
        if start == 'A':
            if random.random() < a:
                scoreA += 1
            else:
                start = 'B'
        else:
            if random.random() < b:
                scoreB += 1
            else:
                start = 'A'

    return scoreA, scoreB


def game_over(a, b):
    return (a >= 15 or b >= 15) and ((a - b >= 2) or (b - a >= 2))


def main():
    print_intro()
    a, b, n = get_inputs()
    winA, winB = simNGames(a, b, n)
    print("A获胜的概率是{0:0.2%}".format(winA / n))
    print("B获胜的概率是{0:0.2%}".format(winB / n))


if __name__ == '__main__':
    main()
