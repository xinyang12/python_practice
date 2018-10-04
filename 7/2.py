def main():
    score = int(input("输入分数: "))
    if score == 5:
        grade = 'A'
    elif score == 4:
        grade = 'B'
    elif score == 3:
        grade = 'C'
    elif score == 2:
        grade = 'D'
    elif score == 1:
        grade = 'E'
    elif score == 0:
        grade = 'F'

    print("等级是:", grade)


if __name__ == '__main__':
    main()
