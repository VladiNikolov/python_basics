import math

required_hours = float(input())
days = int(input())
number_staff = int(input())


all_hours = (days * 8) * 0.90
extraordinary = number_staff * 2 * days
total_hours = all_hours + extraordinary
difference = abs(total_hours - required_hours)

if total_hours >= required_hours:
    print(f"Yes!{math.floor(difference)} hours left.")
else:
    print(f"Not enough time!{math.ceil(difference)} hours needed.")
