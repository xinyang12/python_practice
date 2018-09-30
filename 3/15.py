def main():
    n = int(input("输入需要和的项数: "))
    sum1 = 0
    for i in range(n):
        sum1 += 4 / (((i + 1) * 2 - 1) * ((-1) ** i))

    print(sum1)


main()
