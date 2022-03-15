volume = int(input())
first_pipe = int(input())
second_pipe = int(input())
hours = float(input())

all_water_first_pipe = first_pipe * hours
all_water_second_pipe = second_pipe * hours
all_water = all_water_first_pipe + all_water_second_pipe

all_percents = (all_water / volume) * 100
percents_first_pipe = (all_water_first_pipe / all_water) * 100
percents_second_pipe = (all_water_second_pipe / all_water) * 100
difference = abs(volume - all_water)
if volume >= all_water:
    print(f"The pool is {all_percents:.2f}% full. Pipe 1: {percents_first_pipe:.2f}%. Pipe 2: {percents_second_pipe:.2f}%.")
else:
    print(f"For {hours} hours the pool overflows with {difference:.2f} liters.")