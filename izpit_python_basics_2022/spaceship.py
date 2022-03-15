# •	На първия ред е широчината на кораба - реално число в интервала [1.00... 10.00]
# •	На втория ред е  дължината на кораба - реално число в интервала [1.00…10.00]
# •	На третия ред е височината на кораба - реално число в интервала [1.00…20.00]
# •	На четвъртия ред е средната височина на астронавтите  -  реално число в интервала [1.50 … 1.90]
import math

width = float(input())
length = float(input())
height = float(input())
average = float(input())

volume = width * length * height
volume_per_one_people = (average + 0.40) * 2 * 2
sum_volume = volume / volume_per_one_people

if sum_volume < 3:
    print("The spacecraft is too small.")
elif 3 <= sum_volume <= 10:
    print(f"The spacecraft holds {math.floor(sum_volume)} astronauts.")
elif sum_volume > 10:
    print("The spacecraft is too big.")


