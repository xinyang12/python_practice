def main():
    year = int(input("输入年份: "))
    if year < 1982 or year > 2048:
        print("年份不在可计算的范围内")
        return
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7
    day = (22 + d + e) % 31
    month = (22 + d + e) // 31 + 3
    print("{}年的复活节日期是{}月{}日".format(year, month, day))


if __name__ == '__main__':
    main()

