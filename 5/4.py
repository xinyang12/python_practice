def main():
    phrase = input("输入短语: ")
    phrase = phrase.upper().split()
    answer = ''
    for p in phrase:
        answer += p[0]

    print(answer)


main()
