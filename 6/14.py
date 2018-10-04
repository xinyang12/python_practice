def main():
    file_name = input("输入文件名: ")
    infile = open(file_name, "r")
    data = infile.readlines()
    num_list = []
    for line in data:
        for num in line.split():
            num_list.append(num)

    toNumbers(num_list)
    print(sumList(squareEach(num_list)))


def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = float(strList[i])



def sumList(nums):
    result = 0
    for i in nums:
        result += i

    return result


def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] * nums[i]

    return nums


main()
