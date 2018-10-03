def main():
    message = input("输入一句话: ").split()
    sum1 = 0
    for word in message:
        sum1 += 1

    print("一共有{0}个单词".format(sum1))


main()
