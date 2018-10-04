def main():
    work_time = float(input("输入工作时间: "))
    hour_salary = float(input("输入每小时的薪水: "))
    if work_time <= 40:
        print("总工资是:", work_time * hour_salary)
    else:
        print("总工资是:", (work_time - 40) * hour_salary * 1.5 + 40 * hour_salary)


if __name__ == '__main__':
    main()
