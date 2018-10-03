from graphics import *
import math


def main():
    win = GraphWin()
    point1 = win.getMouse()
    point1.setFill('red')
    point1.draw(win)
    point2 = win.getMouse()
    point2.setFill('red')
    point2.draw(win)
    point3 = win.getMouse()
    point3.setFill('red')
    point3.draw(win)

    polygen = Polygon(point1, point2, point3)
    polygen.draw(win)
    a = math.sqrt((point1.getX() - point2.getX()) ** 2 + (point1.getY() - point2.getY()) ** 2)
    b = math.sqrt((point1.getX() - point3.getX()) ** 2 + (point1.getY() - point3.getY()) ** 2)
    c = math.sqrt((point2.getX() - point3.getX()) ** 2 + (point2.getY() - point3.getY()) ** 2)
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - b))

    print("面积为:", area)
    print("周长为:", a + b + c)
    win.getMouse()
    win.close()


main()
