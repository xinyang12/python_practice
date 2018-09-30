def main():
    h_number = eval(input("输入氢原子的数量: "))
    c_number = eval(input("输入碳原子的数量: "))
    o_number = eval(input("输入氧原子的数量: "))

    h_weight = 1.00794
    c_weight = 12.0107
    o_weight = 15.9994

    print("总分子量为:", h_number * h_weight + c_number * c_weight + o_number * o_weight)


main()
