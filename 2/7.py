def main():
    print("算钱程序")
    principal = eval(input("输入本金: "))
    time = eval(input("输入投资的年数: "))
    apr = eval(input("输入利率: "))
    sum1 = principal
    for i in range(time):
        sum1 += principal * i
        sum1 = sum1 * (1 + apr)
    print(time, "年之后的总钱数是", sum1)


main()
