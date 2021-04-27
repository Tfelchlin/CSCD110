num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
remainder = 0
while num2 != 0:
    remainder = num1 % num2
    num1 = num2
    num2 = remainder
print('The GCD is', num1)
