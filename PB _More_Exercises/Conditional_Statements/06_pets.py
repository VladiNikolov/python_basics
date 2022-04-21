from math import floor,ceil
days = int(input())
left_food = int(input())
dogs_food = float(input())
cats_food = float(input())
turtles_food = float(input())

turtles_food = turtles_food / 1000
all_food = (dogs_food + cats_food + turtles_food) * days
difference = abs(left_food - all_food)
if left_food >= all_food:
    print(f"{floor(difference)} kilos of food left.")
else:
    print(f"{ceil(difference)} more kilos of food are needed.")