def main():
    x1 = eval(input("输入第一个点的x坐标: "))
    y1 = eval(input("输入第一个点的y坐标: "))
    x2 = eval(input("输入第二个点的x坐标: "))
    y2 = eval(input("输入第二个点的y坐标: "))
    print("斜率为", (y2 - y1) / (x2 - x1))


main()
