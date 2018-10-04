def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] * nums[i]

    return nums


def main():
    a_list = [1, 2, 3, 4]
    b_list = squareEach(a_list)
    print(a_list)


main()
