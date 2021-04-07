#get the tax rate from the user.
tax = float(input("Please enter the tax rate: "))
#convert the tax rate into a %
tax = tax / 100
#Get the item's price from the user
Price = float(input("Please enter the item's price: "))
#apply the tax to the item price
total_tax = tax * Price
#add the tax to the item price to get total price
total_price = total_tax + Price
#display the total price
print("The total price is $",format(total_price, '.2f'),sep='')
