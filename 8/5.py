def main():
    n = int(input("输入值: "))
    flag = False
    if n == 1:
        print("1不是素数也不是合数")
        return
    elif n == 2:
        print("2是素数")
        return
    else:
        for i in range(2, n):
            if n % i == 0:
                flag = True
                break

    if flag:
        print("{}不是素数".format(n))
    else:
        print("{}是素数".format(n))


if __name__ == '__main__':
    main()
