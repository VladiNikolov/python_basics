# budget = float(input())
# number_statists = int(input())
# price_dress = float(input())
#
# price_decor = budget * 0.10
# all_price = (price_dress * number_statists) + price_decor
# if number_statists > 150:
#     price_dress = price_dress * 0.90
#     all_price = (price_dress * number_statists) + price_decor
# difference = abs(budget - all_price)
# if all_price > budget:
#     print("Not enough money!")
#     print(f"Wingard needs {difference:.2f} leva more.")
# else:
#     print("Action!")
#     print(f"Wingard starts filming with {difference:.2f} leva left.")

budget = float(input())
number_statists = int(input())
price_dress = float(input())
all_price = 0

price_decor = budget * 0.10
if number_statists <= 150:
    all_price = (price_dress * number_statists) + price_decor
elif number_statists > 150:
    price_dress = price_dress * 0.90
    all_price = (price_dress * number_statists) + price_decor
difference = abs(budget - all_price)
if all_price > budget:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")