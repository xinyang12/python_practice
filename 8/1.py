def main():
    n = int(input("要求第几个斐波那契数字: "))
    index = 2
    a = 1
    b = 1
    answer = b
    while index < n:
        answer = a + b
        a = b
        b = answer
        index += 1

    print(answer)


if __name__ == '__main__':
    main()
