def main():
    n = int(input("输入值: "))
    answer = []
    for i in range(2, n + 1):
        if is_prime_number(i):
            answer.append(i)
            
    print(answer)


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
