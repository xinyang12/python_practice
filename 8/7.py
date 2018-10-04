def main():
    n = int(input("输入值: "))
    if n % 2 == 1:
        print("n不是偶数")
        return
    for i in range(2, n // 2):
        if is_prime_number(i) and is_prime_number(n - i):
            print(i, n - i)


def is_prime_number(n):
    flag = True
    if n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                flag = False
                break

    return flag


if __name__ == '__main__':
    main()
