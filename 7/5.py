def main():
    weight = float(input("输入你的体重(磅): "))
    height = float(input("输入你的身高(英寸): "))
    bmi = calc_bmi(weight, height)
    if bmi < 19:
        print("你的身体在健康范围之下")
    elif 19 <= bmi <= 25:
        print("你的身体很健康")
    else:
        print("你的身体在健康范围之上")


def calc_bmi(weight, height):
    return weight * 720 / (height * height)


if __name__ == '__main__':
    main()
