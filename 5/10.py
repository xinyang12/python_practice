def main():
    message = input("输入一句话: ").split()
    word_count = 0
    char_count = 0
    for word in message:
        word_count += 1
        for ch in word:
            char_count += 1

    print("这句话的单词的平均长度是{}".format(char_count / word_count))


main()
