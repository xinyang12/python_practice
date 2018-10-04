def main():
    file_name = input("输入文件名: ")
    infile = open(file_name, "r")
    start_mile = int(infile.readline())
    total_miles = 0
    total_oil = 0
    travelPG = []
    while True:
        data = infile.readline()
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

    infile.close()
    print("每段旅程的平均消耗:")
    print(travelPG)
    print("总消耗:")
    print(total_miles / total_oil)


if __name__ == '__main__':
    main()
