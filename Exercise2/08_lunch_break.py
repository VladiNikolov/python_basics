from math import ceil

name_movie = input()
duration_movie = int(input())
duration_rest = int(input())

time_lunch = duration_rest * 1/8
time_rest = duration_rest * 1/4
needed_time = time_lunch + time_rest + duration_movie
difference = abs(duration_rest - needed_time)
if needed_time < duration_rest:
    print(f"You have enough time to watch {name_movie} and left with {ceil(difference)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_movie}, you need {ceil(difference)} more minutes.")
