from graphics import *


def main():
    win = GraphWin()
    # 绘制眼睛
    left_eye = Circle(Point(80, 40), 10)
    left_eye.setFill('red')
    left_eye.setOutline('red')
    right_eye = left_eye.clone()
    right_eye.move(40, 0)

    # 绘制脸
    face = Circle(Point(100, 80), 80)

    # 绘制嘴
    mouth = Line(Point(80, 120), Point(120, 120))

    mouth.draw(win)
    face.draw(win)
    left_eye.draw(win)
    right_eye.draw(win)
    win.getMouse()
    win.close()


main()
