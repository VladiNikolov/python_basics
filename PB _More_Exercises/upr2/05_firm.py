import math

needed_hours = int(input())
days = int(input())
workers = int(input())

all_hours = (days * 8) * 0.90
extraordinary_hour = (workers * 2) * days
all_hours = all_hours + extraordinary_hour
difference = abs(needed_hours - math.floor(all_hours) )
if needed_hours <= all_hours:
    print(f"Yes!{difference} hours left.")
else:
    print(f"Not enough time!{difference} hours needed.")