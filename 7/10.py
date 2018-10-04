def main():
    year = int(input("输入年份: "))
    if year < 1900 or year > 2099:
        print("年份不在可计算的范围内")
        return
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7
    raw_day = 22 + d + e
    if year == 1954 or year == 1981 or year == 2049 or year == 2076:
        raw_day -= 7
    day = raw_day % 31
    month = raw_day // 31 + 3
    print("{}年的复活节日期是{}月{}日".format(year, month, day))


if __name__ == '__main__':
    main()

