def main():
    age = int(input("输入年龄: "))
    citizen_year = int(input("输入公民年数: "))
    can_flag = False
    zhong_flag = False
    if age >= 30:
        if citizen_year >= 9:
            can_flag = True
    if age >= 25:
        if citizen_year >= 7:
            zhong_flag = True

    if can_flag and zhong_flag:
        print("可以成为参议员和众议员")
    elif can_flag:
        print("可以成为参议员")
    elif zhong_flag:
        print("可以成为众议员")
    else:
        print("不能当议员")


if __name__ == '__main__':
    main()
