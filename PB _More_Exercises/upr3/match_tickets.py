# •	На първия ред е бюджетът – реално число в интервала [1 000.00 ... 1 000 000.00]
# •	На втория ред е категорията – "VIP" или "Normal"
# •	На третия ред е броят на хората в групата – цяло число в интервала [1 ... 200]
#     От1 до 4 – 75% от бюджета.
# •	От 5 до 9 – 60% от бюджета.
# •	От 10 до 24 – 50% от бюджета.
# •	От 25 до 49 – 40% от бюджета.
# •	50 или повече – 25% от бюджета.

budget = float(input())
category = input()
number_people = int(input())
all_price = 0

if 1 <= number_people <= 4:
    budget = budget * 0.25
    if category == "VIP":
        all_price = number_people * 499.99
    elif category == "Normal":
        all_price = number_people * 249.99
elif number_people <= 9:
    budget = budget * 0.40
    if category == "VIP":
        all_price = number_people * 499.99
    elif category == "Normal":
        all_price = number_people * 249.99
elif number_people <= 24:
    budget = budget * 0.50
    if category == "VIP":
        all_price = number_people * 499.99
    elif category == "Normal":
        all_price = number_people * 249.99
elif number_people <= 49:
    budget = budget * 0.60
    if category == "VIP":
        all_price = number_people * 499.99
    elif category == "Normal":
        all_price = number_people * 249.99
elif number_people > 50:
    budget = budget * 0.75
    if category == "VIP":
        all_price = number_people * 499.99
    elif category == "Normal":
        all_price = number_people * 249.99

difference = abs(budget - all_price)
if budget >= all_price:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")


