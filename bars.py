# We are going to create a menu that will re-display
# Menu will have three choices
# Create some constants to represent these choices

Fraunces = 1
Petes = 2
Mcsorleys = 3
Quit = 0

# We will set our choice variable so our menu displays
choice = 7
while choice != Quit:
    print()
    print("     Get the Facts Menu")
    print("1. Frances Tavern NYC Founded 1762")
    print("2. Pete's Tavern Founded in 1864.")
    print("3. Mcsorley's Old Ale Houlse 1854.")
    choice = int(input("Please enter a valid choice 1 ~ 3 or 0: "))
    if choice == Fraunces:
        print()
        print('this is a fact')
        print("Another cool fact")
    elif choice == Petes:
        print()
        print("Fun facts")
    elif choice == Mcsorleys:
        print()
        print("Last fact")
    elif choice == Quit:
        print("have a good night")
    else:
        print("Try again")
