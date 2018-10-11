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
        # todo 按理说获胜的概率应该是加起来等于1，但是按照书上的说法不是这样，
        # 但是如果不是这样，这里的概率就没法算了
        if scoreA > scoreB:
            winA += 1
        else:
            winB += 1

    return winA, winB


def simOneGame(a, b):
    scoreA = scoreB = 0
    while not game_over(scoreA, scoreB):
        if random.random() < a:
            scoreA += 1
        else:
            scoreB += 1

    return scoreA, scoreB


def game_over(a, b):
    return (a >= 25 or b >= 25) and ((a - b >= 2) or (b - a >= 2))


def main():
    print_intro()
    a, b, n = get_inputs()
    winA, winB = simNGames(a, b, n)
    print("A获胜的概率是{0:0.2%}".format(winA / n))
    print("B获胜的概率是{0:0.2%}".format(winB / n))


if __name__ == '__main__':
    main()
