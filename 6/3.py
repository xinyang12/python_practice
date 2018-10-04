import math


def sphereArea(radius):
    return 4 * math.pi * radius * radius


def sphereVolume(radius):
    return 4 / 3 * math.pi * radius * radius * radius


def main():
    r = eval(input("输入半径: "))
    print("体积是", sphereVolume(r))
    print("表面积是", sphereArea(r))


main()
