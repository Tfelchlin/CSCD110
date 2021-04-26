# This is a guessing game
# A break can sometimes yeild a loop that is easier to understand
# A break statement causes the loop to exit immediatley
import random
# Get the limits from the user
little = int(input("Please enter the smaller number: "))
big = int(input("Please enter the bigger number: "))
computerNumber = random.randint(little,big)

count = 0
while True:
    count += 1
    userNumber = int(input("Enter your guess: "))
    if userNumber > computerNumber:
        print("Too large")
    elif userNumber < computerNumber:
        print("Too small")
    else:
        print("You guessed correct" ,"it took", count,"tries")
        break
