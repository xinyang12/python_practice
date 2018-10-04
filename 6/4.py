def sumN(n):
    result = 0
    for i in range(n + 1):
        result += i

    return result


def sumNCubes(n):
    result = 0
    for i in range(n + 1):
        result += i * i * i

    return result


def main():
    x = int(input("输入n: "))
    print("前n个自然数的和是:", sumN(x))
    print("前n个自然数的立方和是:", sumNCubes(x))


main()
