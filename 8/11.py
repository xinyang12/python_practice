def main():
    heating_serial = []
    cooling_serial = []
    while True:
        temp = input("输入温度: ")
        if temp == '':
            break
        temp = int(temp)
        if temp < 60:
            heating_serial.append(60 - temp)
        elif temp > 80:
            cooling_serial.append(temp - 80)

    print("heating degree-days")
    print(heating_serial)
    print("cooling degree-days")
    print(cooling_serial)


if __name__ == '__main__':
    main()
