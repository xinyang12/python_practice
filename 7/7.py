def main():
    try:
        start_hour, start_minute, end_hour, end_minute = get_time()
        if start_hour >= 21:
            work_time = ((end_hour * 60 + end_minute) - (start_hour * 60 + start_minute)) / 60
            salary = work_time * 1.75
        elif end_hour >= 21:
            before_work_time = (21 * 60 - (start_hour * 60 + start_minute)) / 60
            after_work_time = (end_hour * 60 + end_minute - 21 * 60) / 60
            salary = before_work_time * 2.50 + after_work_time * 1.75
        else:
            work_time = ((end_hour * 60 + end_minute) - (start_hour * 60 + start_minute)) / 60
            salary = work_time * 2.50
    
        print("总薪水是:", salary)
    except:
        print("输入有误")


def get_time():
    start_hour, start_minute = input("输入开始时间: (hh:mm)").split(":")
    end_hour, end_minute = input("输入结束时间: (hh:mm)").split(":")
    start_hour = int(start_hour)
    start_minute = int(start_minute)
    end_hour = int(end_hour)
    end_minute = int(end_minute)
    return start_hour, start_minute, end_hour, end_minute


if __name__ == '__main__':
    main()
