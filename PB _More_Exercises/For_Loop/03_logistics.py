count_loads = int(input())
sum_loads_microbus = 0
sum_loads_truck = 0
sum_loads_train= 0
num_loads = 0
for tonnage in range(1, count_loads + 1):
    current_tonnage = int(input())
    if 0 < current_tonnage <= 3:
        sum_loads_microbus += current_tonnage
    elif current_tonnage <= 11:
        sum_loads_truck += current_tonnage
    elif current_tonnage >= 12:
        sum_loads_train += current_tonnage
sum_all_loads = (sum_loads_microbus * 200) + (sum_loads_truck * 175) + (sum_loads_train * 120)
all_loads = sum_loads_microbus + sum_loads_truck + sum_loads_train
average_price = sum_all_loads / all_loads
print(f"{average_price:.2f}")
print(f"{sum_loads_microbus / all_loads * 100:.2f}%")
print(f"{sum_loads_truck / all_loads * 100:.2f}%")
print(f"{sum_loads_train / all_loads * 100:.2f}%")

