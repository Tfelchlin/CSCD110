# Get two non-zero intergers from the user
ya_1 = int(input("Please enter a non-zero interger: "))
ya_2 = int(input("Please enter another non-zero interger: "))
# Display the results of Adding the second interger the the first one
print(f'{ya_1} plus {ya_2} equals',ya_1 + ya_2)
# Display the subtraction of the second and the first intergers
print(f'{ya_1} minus {ya_2} equals',ya_1 - ya_2)
# Display the product of the two
print(f'{ya_1} multiplied {ya_2} equals',ya_1 * ya_2)
# Display the first int raised to the second
print(f"{ya_1} raised to {ya_2} is",ya_1 ** ya_2)
# Display inter division of the first int by the second
# Also i need to combine the operations of the remander with the rest and add seperaters 
print(f'{ya_1} divided by {ya_2} equals ',ya_1 // ya_2,","," and with a remainder of ",ya_1 % ya_2,'.',sep='')

