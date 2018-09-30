def main():
    n = int(input("有多少个数字要求和: "))
    sum1 = 0
    for i in range(1, n + 1):
        num = float(input("请输入值: "))
        sum1 += num

    print("平均值为:", sum1 / n)


main()
