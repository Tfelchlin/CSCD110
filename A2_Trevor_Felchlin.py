# Get hole number
Hole = input("Enter the hole played:")
# Get the par vlaue for the hole
Par = int(input("Enter the par value for the hole:"))
# Get the number of strokes it took to complete the hole
Strokes = int(input("Enter the number of stokes it took to complete the hole:" ))
# if we subtract the par value form the stokes it give is score value 
scorevalue = Strokes - Par
# our decision structure is an if / elif / else structure
if scorevalue == 5:
    topar = ("5 over par")
elif scorevalue == 4:
    topar =("4 over par")
elif scorevalue == 3:
    topar =("triple bogey")
elif scorevalue == 2:
    topar =("double bogey")
elif scorevalue == 1:
    topar =("bogey")
elif scorevalue == 0:
    topar =("par")
elif scorevalue == -1:
    topar =("birdie")
elif scorevalue == -2:
    topar =("eagle")
elif scorevalue == -3:
    topar =("double eagle or an albatross ")
elif scorevalue == -4:
    topar =("condor")
elif scorevalue == -5:
    topar =("ostrich")
else:
    topar =("BAD SCORE")
print(f"On hole number {Hole} which is a par {Par} you got a {topar}.")
