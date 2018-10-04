def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = float(strList[i])


def main():
    a_list = ['12', '13', '1.2']
    toNumbers(a_list)
    print(a_list)
    for i in a_list:
        print(type(i))


main()
