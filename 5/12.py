def main():
    principal = eval(input("输入本金: "))
    apr = eval(input("输入利率: "))
    year = eval(input("输入投资年数: "))

    print("{0:8}{1:^8}".format("Year", "Value"))
    print("-" * 16)
    for i in range(year):
        principal = principal * (1 + apr)
        print("{0:<8}${1:^4.2f}".format(i, principal))


main()
