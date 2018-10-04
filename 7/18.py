# 随便找段代码来try
def main():
    try:
        phrase = input("输入短语: ")
        print(acronym(phrase))
    except:
        print("输入有误")



def acronym(phrase):
    phrase = phrase.upper().split()
    answer = ''
    for p in phrase:
        answer += p[0]

    return answer


main()
