def main():
    n = int(input("输入数字: "))
    sum1 = 0
    for i in range(1, n + 1):
        sum1 += i * i * i

    print(sum1)


main()
