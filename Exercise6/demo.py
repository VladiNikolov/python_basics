import math

number_of_people = int(input())
entrans_tax = float(input())
price_deck_chair = float(input())
price_umbrella = float(input())

total_sum = number_of_people * entrans_tax
needed_desk_chair = math.ceil(number_of_people * 0.75)
all_sum_desk_chair = needed_desk_chair * price_deck_chair

needed_umbrella = math.ceil(number_of_people * 0.5)
all_sum_umbrella = needed_umbrella * price_umbrella

total = total_sum + all_sum_desk_chair + all_sum_umbrella
print(f"{total:.2f} lv.")
