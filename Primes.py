lower = 1
upper = int(input("Please enter a number: "))
print(f"Prime numbers between one and {upper} are:")

for num in range(lower, upper + 1):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)
