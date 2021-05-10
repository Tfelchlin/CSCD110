temp_fc = 1
temp_cf = 2
light_to_miles = 3
meter_ft = 4
Quit = 0

def main():
    choice = 13
    while choice != Quit:
        Menu_display()
        choice = int(input("Please enter a vaild choice: "))
        if choice == temp_fc:
           temp_f = float(input("Please enter a temp in F: "))
           print(f"{temp_f} degrees Fahrenheit is equal to {temp_in_C(temp_f):.2f} degrees celsius.")
        elif choice == temp_cf:
            temp_c = float(input("Please enter temp in C: "))
            print(f"{temp_c} degrees celsius is equal to {temp_in_F(temp_c): .2f} degrees Fahrenheit.")
        elif choice == light_to_miles:
            light_in_miles = int(input("Please enter amout of light years: "))
            print(f"{light_in_miles}light years is eual to {light_miles(light_in_miles)} miles.")
        elif choice == meter_ft:
            meters=float(input("Please enter amount of meters: "))
            print(f"{meters} meters is equal to {ft_from_meters(meters):.2f} feet.")
        
def Menu_display():
    print("        Menu            ")
    print("1.Convert Fahrenheit to Celsius.")
    print("2.Convert Celsius to Fahrenheit. ")
    print("3.Convert Light Years to Miles. ")
    print("4.Convert Meters to Feet. ")
    print("5. ")

def temp_in_C(Fahrenheit):
    return (Fahrenheit - 32) * 5/9

def temp_in_F(Celsius):
    return (Celsius * 9/5) + 32

def light_miles(light_years):
    return light_years * 5,878,625,370,000
def ft_from_meters(Meters):
    return Meters * 3.28084




main()
