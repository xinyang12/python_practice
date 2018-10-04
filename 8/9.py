def main():
    start_mile = int(input("输入初始里程: "))
    total_miles = 0
    total_oil = 0
    travelPG = []
    while True:
        data = input("输入目前的里程和油量: ")
        if data == '':
            break
        miles, oil = data.split()
        miles = int(miles)
        oil = int(oil)
        total_miles += miles - start_mile
        total_oil += oil
        travelPG.append((miles - start_mile) / oil)
        start_mile = miles

    if total_oil == 0 or total_miles == 0:
        print("车没动弹")
        return
    print("每段旅程的平均消耗:")
    print(travelPG)
    print("总消耗:")
    print(total_miles / total_oil)


if __name__ == '__main__':
    main()
