def main():
    a = 1
    b = 1
    sum1 = a
    n = int(input("要求第几个斐波那契数字: "))
    for i in range(2, n):
        sum1 = a + b
        a = b
        b = sum1

    print(sum1)


main()
