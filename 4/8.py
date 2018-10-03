from graphics import *
import math


def main():
    # 由于屏幕坐标系和真实坐标系的上下相反，因此计算出来的斜率符号也是相反的
    win = GraphWin()
    point1 = win.getMouse()
    point1.setFill('red')
    point1.draw(win)
    point2 = win.getMouse()
    point2.setFill('red')
    point2.draw(win)

    line = Line(point1, point2)
    middle_point = Point((point1.getX() + point2.getX()) / 2, (point1.getY() + point2.getY()) / 2)
    middle_point.setFill('#00FFFF')

    line.draw(win)
    middle_point.draw(win)

    slope = (point1.getY() - point2.getY()) / (point1.getX() - point2.getX())
    length = math.sqrt((point1.getY() - point2.getY()) ** 2 + (point1.getX() - point2.getX()) ** 2)

    print("斜率是", slope)
    print("长度是", length)
    win.getMouse()
    win.close()


main()
