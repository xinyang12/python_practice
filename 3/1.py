import math


def main():
    r = eval(input("输入半径: "))
    v = 4 / 3 * math.pi * r * r * r
    a = 4 * math.pi * r * r
    print("体积是", v)
    print("表面积是", a)


main()
