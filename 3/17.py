def main():
    n = int(input("输入猜测的次数: "))
    x = float(input("输入要求根的数字: "))
    guess = x / 2
    for i in range(n):
        guess = (guess + x / guess) / 2

    print(guess)


main()
