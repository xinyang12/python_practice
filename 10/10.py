import math


class Cube:
    def __init__(self, side):
        self.side = side

    def getSide(self):
        return self.side

    def surfaceArea(self):
        return 8 * self.side * self.side

    def volume(self):
        return self.side * self.side * self.side


def main():
    side = float(input("输入立方体的半径: "))
    cube = Cube(side)
    print("该立方体的表面积是:", cube.surfaceArea())
    print("该立方体的体积是: ", cube.volume())


if __name__ == "__main__":
    main()
