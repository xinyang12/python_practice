def main():
    score = int(input("输入分数: "))
    print("对应的等级是:", grade(score))


def grade(score):
    grade_score = ['F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F',
             'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F',
             'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F',
             'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F',
             'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F',
             'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F',
             'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D',
             'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C',
             'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B',
             'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A']
    return grade_score[score]


main()
