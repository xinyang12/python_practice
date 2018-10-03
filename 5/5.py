def main():
    name = input("输入单个名字: ")
    sum1 = 0
    for ch in name:
        sum1 += ord(ch.lower()) - ord('a') + 1

    print(sum1)


main()
