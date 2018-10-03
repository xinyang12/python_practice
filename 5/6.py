def main():
    name = input("输入完整名字: ").split()
    sum1 = 0
    for word in name:
        for ch in word:
            sum1 += ord(ch.lower()) - ord('a') + 1

    print(sum1)


main()
