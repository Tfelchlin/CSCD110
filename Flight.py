'''Flights are scheduled to land at a specific time
Flights care then estimated to land at a specific time
Flights can be earlt, on time, or delayed.
Precondition
0.0 <= scheduled_time < 24.0
0.0 <= estimated_time < 24.0
'''
schedual_time = float(input("please enter the fight's scheduled time: "))
estimated_time = float(input("please enter the fight's estimated time: "))

# on time
if schedual_time == estimated_time:
    print("Fight is on time")
# dealyed
elif schedual_time < estimated_time:
    print("Fight is dealyed")
# early
else:
    print("Flight is coming sooner yay")
