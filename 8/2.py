import math


def main():
    print("{0:^20}".format("风速 | 温度"), end="")
    for i in range(-20, 61, 10):
        print("{0:<10}".format(i), end="")
    print()
    for i in range(0, 51, 5):
        print("{0:^20}".format(i), end="")
        for j in range(-20, 61, 10):
            if i == 0:
                print("{0:^10}".format("None"), end="")
            else:
                print("{0:^10.4f}".format(calc(j, i)), end="")
        print()


def calc(t, v):
    return 35.74 + 0.6215 * t - 35.75 * math.pow(v, 0.16) + 0.4275 * t * math.pow(v, 0.16)


if __name__ == '__main__':
    main()
