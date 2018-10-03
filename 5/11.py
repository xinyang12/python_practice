def main():
    print("This program illustrates a chaotic function")
    x, y = input("输入两个值: ").split(",")
    times = int(input("输入迭代次数: "))
    x, y = float(x), float(y)
    print("{0:6}{1:^10}{2:^10}".format("index", x, y))
    print('-' * 26)
    for i in range(times):
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)
        print("{0:<6}{1:10.6f}{2:10.6f}".format(i + 1, x, y))


main()
