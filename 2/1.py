def main():
    print("这是一个将摄氏度转换为华氏度的程序")
    print("This is a program that convert celsius to fahrenheit")
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")


main()
