months = int(input())

water = 20
internet = 15
electricity = 0
for number in range(1, months + 1):
    input_electricity = float(input())
    electricity += input_electricity
all_internet = internet * months
all_water = water * months
other = (all_water + all_internet + electricity) * 1.20
print(f"Electricity: {electricity:.2f} lv")
print(f"Water: {all_water:.2f} lv")
print(f"Internet: {all_internet:.2f} lv")
print(f"Other: {other:.2f} lv")
average = all_water + all_internet + electricity + other
print(f"Average: {average / months:.2f} lv")