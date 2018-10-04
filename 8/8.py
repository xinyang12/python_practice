def main():
    print("求最大公约数")
    n, m = input("输入两个数字").split(",")
    n = int(n)
    m = int(m)
    while m != 0:
        n, m = m, n % m

    print(n)


if __name__ == '__main__':
    main()
