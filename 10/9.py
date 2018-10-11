import math


class Globe:
    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def surfaceArea(self):
        return 4 * math.pi * self.radius * self.radius

    def volume(self):
        return 4 / 3 * math.pi * self.radius * self.radius * self.radius


def main():
    radius = float(input("输入球体的半径: "))
    globe = Globe(radius)
    print("该球体的表面积是:", globe.surfaceArea())
    print("该球体的体积是: ", globe.volume())


if __name__ == "__main__":
    main()
