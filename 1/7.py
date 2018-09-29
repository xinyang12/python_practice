def main():
    print("This program illustrates a chaotic function")
    # n = eval(input("How many numbers should I print? "))
    x = eval(input("Enter a number between 0 and 1: "))
    y = eval(input("Enter a number between 0 and 1: "))
    print("input    ", x, "     ", y)
    print("----------------------------")
    for i in range(100):
        x = 3.9 * (x - x * x)
        y = 3.9 * (y - y * y)
        print(x, "      ", y)


main()
