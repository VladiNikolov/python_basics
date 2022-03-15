number_of_loads = int(input())

price_microbus = 0
price_truck = 0
price_train = 0

sum_tonnage_microbus = 0
sum_tonnage_truck = 0
sum_tonnage_train = 0
all_tonnage = 0
for number in range(number_of_loads):
    tonnage = int(input())
    all_tonnage += tonnage
    if tonnage <= 3:
        sum_tonnage_microbus += tonnage
        price_microbus = 200
    elif tonnage <= 11:
        sum_tonnage_truck += tonnage
        price_truck = 175
    else:
        sum_tonnage_train += tonnage
        price_train = 120
equal_tons = (price_microbus * sum_tonnage_microbus + price_truck * sum_tonnage_truck + \
             price_train * sum_tonnage_train) / all_tonnage
print(f'{equal_tons:.2f}')
print(f'{sum_tonnage_microbus / all_tonnage *100:.2f}%')
print(f'{sum_tonnage_truck / all_tonnage *100:.2f}%')
print(f'{sum_tonnage_train / all_tonnage *100:.2f}%')





