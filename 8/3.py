def main():
    lilv = float(input("输入年利率: "))
    benjin = 1
    year = 0
    while benjin < 2:
        benjin *= (1 + lilv)
        year += 1

    print("需要{}年可以收益翻倍".format(year))


if __name__ == '__main__':
    main()
