def main():
    benjin = eval(input("输入本金: "))
    meinianlilv = eval(input("输入每年的利率: "))
    times = eval(input("输入利息每年复利的次数: "))
    avgLilv = meinianlilv / times
    print("每年的利率为", meinianlilv)
    print("每年复利的次数为", times)
    print("平均每次利率为", avgLilv)
    for i in range(times * 10):
        benjin = benjin * (1 + avgLilv)
    print(benjin)


main()
