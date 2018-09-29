def main():
    print("这是一个将华氏度转换为摄氏度的程序")
    print("This is a program that convert fahrenheit to celsius")
    fahrenheit = eval(input("What is the Fahrenheit temperature? "))
    celsius = (fahrenheit - 32) * 5 / 9
    print("The temperature is", celsius, "degrees Celsius.")


main()
