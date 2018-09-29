def main():
    print("This program calculates the future value")
    principal = eval(input("Enter the initial principal: "))
    time = eval(input("Enter the number of year: "))
    apr = eval(input("Enter the annual interest rate: "))
    for i in range(time):
        principal = principal * (1 + apr)
    print("The value in", time, "years is:", principal)


main()
