import math


def calc_area(d):
    return math.pi * (d / 2) * (d / 2)


def calc_cost(s, p):
    return p / s


def main():
    d = eval(input("输入直径: "))
    p = eval(input("输入价格: "))
    s = calc_area(d)
    print("每平方英寸的成本是", calc_cost(s, p))


main()
