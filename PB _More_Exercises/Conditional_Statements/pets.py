# •	Първи ред – брой дни – цяло число в интервал [1…5000]
# •	Втори ред – оставена храна в килограми – цяло число в интервал [0…100000]
# •	Трети ред – храна на ден за кучето в килограми – реално число в интервал [0.00…100.00]
# •	Четвърти ред – храна на ден за котката в килограми– реално число в интервал [0.00…100.00]
# •	Пети ред – храна на ден за костенурката в грамове – реално число в интервал [0.00…10000.00]
#
import math

days = int(input())
total_food = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input())

animal_food_per_day = dog_food_per_day + cat_food_per_day + (turtle_food_per_day / 1000)
all_food = days * animal_food_per_day
food = abs(total_food - all_food)

if total_food >= all_food:
    print(f"{math.floor(food)} kilos of food left.")
else:
    print(f"{math.ceil(food)} more kilos of food are needed.")



