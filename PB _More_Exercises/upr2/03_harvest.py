import math

vine_square = int(input())
grape_per_1square = float(input())
needed_liters_wine = int(input())
number_workers = int(input())

all_grapes = vine_square * grape_per_1square
grapes_for_wine = all_grapes * 0.40
wine_liters = grapes_for_wine / 2.5
difference = abs(wine_liters - needed_liters_wine)
if wine_liters < needed_liters_wine:
    print(f"It will be a tough winter! More {math.floor(difference)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {math.floor(needed_liters_wine + difference)} liters.")
    print(f"{math.ceil(difference)} liters left -> {math.ceil(difference/number_workers)} liters per person.")
