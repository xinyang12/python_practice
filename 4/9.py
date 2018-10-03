from graphics import *


def main():
    win = GraphWin()
    point1 = win.getMouse()
    point2 = win.getMouse()
    a = abs(point1.getX() - point2.getX())
    b = abs(point1.getY() - point2.getY())
    rec = Rectangle(point1, point2)
    rec.draw(win)
    print("面积为:", a * b)
    print("周长为:", 2 * (a + b))
    win.getMouse()
    win.close()


main()
