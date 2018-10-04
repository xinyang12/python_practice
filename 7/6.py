def calc_fine(speed_limit, speed):
    cost = 0
    if speed > 90:
        cost += 200
    if speed > speed_limit:
        outter_speed = speed - speed_limit
        cost += 5 * (outter_speed)
    return cost


def main():
    speed_limit = int(input("输入速度限制: "))
    speed = int(input("输入速度: "))
    print("要罚款{}美元".format(calc_fine(speed, speed_limit)))


if __name__ == '__main__':
    main()

