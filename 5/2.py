def main():
    # 原题中1和0对应的等级都是F，不知道是写错了，还是有意为之
    grade = ['F', 'F', 'D', 'C', 'B', 'A']
    score = int(input("输入分数: "))
    print("对应的等级是:", grade[score])


main()
