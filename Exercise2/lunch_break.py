import math

name = input()
time_episode = int(input())
time_break = int(input())

time_for_lunch = time_break * 1/8
time_for_rest = time_break * 1/4
all_time_rest = time_break - (time_for_lunch + time_for_rest)
difference = abs(time_episode - all_time_rest)
if time_episode <= all_time_rest:
    print(f'You have enough time to watch {name} and left with {math.ceil(difference)} minutes free time.')
else:
    print(f"You don't have enough time to watch {name}, you need {math.ceil(difference)} more minutes.")