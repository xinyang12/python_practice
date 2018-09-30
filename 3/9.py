import math


def main():
    a = float(input("输入第一条边的长度: "))
    b = float(input("输入第二条边的长度: "))
    c = float(input("输入第三条边的长度: "))
    s = (a + b + c) / 2
    a = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("面积为", a)


main()
