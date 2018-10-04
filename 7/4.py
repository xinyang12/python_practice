def calc_grade(score):
    if score < 7:
        grade = '大一'
    elif 7 <= score <= 16:
        grade = '大二'
    elif 16 < score <= 26:
        grade = '大三'
    elif score > 25:
        grade = '大四'
    else:
        grade = '不知道你是大几'

    return grade


def main():
    score = int(input("输入学分: "))
    print(calc_grade(score))


if __name__ == '__main__':
    main()
