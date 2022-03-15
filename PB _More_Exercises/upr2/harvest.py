import math

area_vine = int(input())
grape_square_meters = float(input())
neded_wine = int(input())
workers = int(input())

total_grapes = area_vine * grape_square_meters
total_grapes_for_wine = total_grapes * 0.40
all_liter_wines = total_grapes_for_wine / 2.5

difference = abs(all_liter_wines - neded_wine)
workers_wine = abs(difference / workers)
if all_liter_wines < neded_wine:
    print(f"It will be a tough winter! More {math.floor(difference)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {math.ceil(all_liter_wines)} liters.")
    print(f"{math.ceil(difference)} liters left -> {math.ceil(workers_wine)} liters per person.")