def main():

    month, day, year = input("输入日期(月/日/年): ").split("/")
    month = int(month)
    day = int(day)
    year = int(year)
    if is_valid_date(year, month, day):
        dayNum = 31 * (month - 1) + day
        if month > 2:
            dayNum -= ((4 * month + 23) // 10)
        if is_leap_year(year) and month > 2:
            dayNum += 1
        print("这天是这年的第{}天".format(dayNum))
    else:
        print("日期不合法")


def is_valid_date(year, month, day):
    # 如果是闰年，将2月时间改为29天
    month2day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        month2day_list[1] = 29
    if month > 12 or month < 1:
        return False
    if day > month2day_list[month - 1] or day < 1:
        return False
    return True


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
