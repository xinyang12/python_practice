def main():
    year = int(input("输入年份: "))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("闰年")
            else:
                print("平年")
        else:
            print("闰年")
    else:
        print("平年")


if __name__ == '__main__':
    main()

