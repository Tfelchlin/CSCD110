# Hey i also did the extra credit!!!


# Ask for the numbers from the user
number1 = int(input("Please enter a non-negative integer: "))
# Got to figure out how to make them re-enter if they type a bad number
if number1 < 0:
    number1 = int(input("I am sorry that is wrong try again: "))
else:
    number1 = number1
    
# Assign the numbers to the menu
factorial = 1
prime_numbers = 2
intsum = 3
Quit = 0
# Make the menu so it displays
choice = 10
while choice != Quit:
    print()
    print("    Welcome to interger fun!!")
    print("1. Print the factorial of the integer")
    print(f"2. Print the prime numbers between 2 and {number1}")
    print(f"3. Print the sum of the integer from 1 to {number1}")
    choice = int(input("Please enter a vaild choice between 1 ~ 3 or 0 to quit: "))
# Use what I know from the time we did factorials to make a factorial calculator
    if choice == factorial:
        product = 1
        for num in range(1,number1 + 1):
            product *= num
        print(product)
# Use the for loop we did for a prime number calculator 
    elif choice == prime_numbers:
        for num in range(1, number1 + 1):
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                print(num)
# Use the basic counting and adding program we learned
    elif choice == intsum:
        x = 1
        total = 0
        while x <= number1:
            total +=x
            x+= 1
        print(total)
# add the quit part
    elif choice == Quit:
        print("Thanks for playing have a great day!")
# Add the try again part
    else:
        print("Please enter a vaild number on the menu")
