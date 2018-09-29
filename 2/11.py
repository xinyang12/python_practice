def main():
    print("这个程序将美元转换成人民币")
    dollars = eval(input("输入美元数: "))
    # 根据2018-09-29指数~~
    rmb = dollars * 6.8688
    print(rmb)


main()
