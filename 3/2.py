import math


def main():
    d = eval(input("输入直径: "))
    p = eval(input("输入价格: "))
    s = math.pi * (d / 2) * (d / 2)
    print("每平方英寸的成本是", p / s)


main()
