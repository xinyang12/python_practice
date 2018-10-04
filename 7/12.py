def main():
    month2day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month, day, year = input("输入日期(月/日/年): ").split("/")
    month = int(month)
    day = int(day)
    year = int(year)
    # 如果是闰年，将2月时间改为29天
    if is_leap_year(year):
        month2day_list[1] = 29
    if month > 12 or month < 1:
        print("日期不合法")
        return
    if day > month2day_list[month - 1] or day < 1:
        print("日期不合法")
        return
    print("日期合法")


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


if __name__ == '__main__':
    main()
