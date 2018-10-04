def calc_fibonacci(n):
    a = 1
    b = 1
    sum1 = a
    for i in range(2, n):
        sum1 = a + b
        a = b
        b = sum1

    return sum1


def main():
    n = int(input("要求第几个斐波那契数字: "))
    print(calc_fibonacci(n))


main()
