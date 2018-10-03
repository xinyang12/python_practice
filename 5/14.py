def main():
    file_name = input("输入文件名: ")
    infile = open(file_name, "r")
    line_count = 0
    word_count = 0
    char_count = 0
    for line in infile:
        line_count += 1
        word = line.split()
        word_count += len(word)
        for ch in line:
            char_count += 1

    print("行数是:", line_count)
    print("单词数是:", word_count)
    print("字符数是:", char_count)


main()
