def main():
    print("这是一个将摄氏度转换为华氏度的程序")
    print("This is a program that convert celsius to fahrenheit")
    for celsius in range(0, 101, 10):
        fahrenheit = 9/5 * celsius + 32
        print(celsius, fahrenheit)


main()
