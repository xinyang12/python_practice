import math


def main():
    degrees = float(input("输入以度为单位的角度: "))
    height = float(input("输入梯子的高度: "))
    radians = math.pi / 180 * degrees
    print("梯子所需的长度为", height / math.sin(radians))


main()
