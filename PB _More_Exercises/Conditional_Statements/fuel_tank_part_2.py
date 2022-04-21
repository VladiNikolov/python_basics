# •	Типа на горивото – текст с възможности: "Gas", "Gasoline" или "Diesel"
# •	Количество гориво – реално число в интервала [1.00 … 50.00]
# •	Притежание на клубна карта – текст с възможности: "Yes" или "No"

name_fuel = input()
quantity = float(input())
card = input()
price = 0

if name_fuel == "Gas":
    if card == "Yes":
        price = 0.93
        price = (price - 0.08) * quantity
    elif card == "No":
        price = 0.93
        price = price * quantity
elif name_fuel == "Gasoline":
    if card == "Yes":
        price = 2.22
        price = (price - 0.18) * quantity
    elif card == "No":
        price = 2.22
        price = price * quantity
elif name_fuel == "Diesel":
    if card == "Yes":
        price = 2.33
        price = (price - 0.12) * quantity
    elif card == "No":
        price = 2.33
        price = price * quantity

if 20 <= quantity <= 25:
    price = price * 0.92
elif quantity > 25:
    price = price * 0.90
print(f"{price:.2f} lv.")