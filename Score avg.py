numberofquizzes=int(input("Enter the amount of quizzes: "))
total=0
quizcount=1
while quizcount <= numberofquizzes:
    scorestring=int(input("Enter the score on quiz " + str(quizcount)+": "))
    score = float(scorestring)
    total = total + score
    quizcount = quizcount + 1
    average = total / numberofquizzes
    if quizcount == (numberofquizzes + 1):
        print("The average quiz score is " + str(average))

