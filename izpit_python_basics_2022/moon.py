# •	На първия ред - средната скорост на движение - реално число в интервала [1000.00... 30000.00]
# •	На втория ред - литри гориво нужни за 100 км - реално число в интервала [1.00…20.00]
import math
middle_speed = float(input())
fuel = float(input())

all_distance = 384400 * 2
all_time = all_distance / middle_speed
total_time = math.ceil(all_time) + 3

all_fuel = (fuel * all_distance) / 100
print(total_time)
print(int(all_fuel))