import os


def main():
    print("这是一个将摄氏度转换为华氏度的程序")
    print("This is a program that convert celsius to fahrenheit")
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")


main()
# os.system("pause")
x = input("Press <Enter> to quit")

# 这两种方法都试了，都不行，不知道为啥