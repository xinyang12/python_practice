def main():
    phrase = input("输入短语: ")

    print(acronym(phrase))


def acronym(phrase):
    phrase = phrase.upper().split()
    answer = ''
    for p in phrase:
        answer += p[0]

    return answer


main()
