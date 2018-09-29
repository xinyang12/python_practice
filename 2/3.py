def main():
    print("This program computes the average of two exam scores.")
    # score1, score2, score3 = eval(input("Enter two scores separated by a comma: "))
    score1 = eval(input("Enter score 1: "))
    score2 = eval(input("Enter score 2: "))
    score3 = eval(input("Enter score 3: "))
    average = (score1 + score2 + score3) / 3
    print("The average of the scores is:", average)


main()
