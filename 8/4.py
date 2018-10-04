def main():
    x = int(input("输入初始值: "))
    serial_num = [x]
    while x != 1:
        if x % 2 == 0:
            x = x // 2
            serial_num.append(x)
        else:
            x = 3 * x + 1
            serial_num.append(x)

    print(serial_num)


if __name__ == '__main__':
    main()
