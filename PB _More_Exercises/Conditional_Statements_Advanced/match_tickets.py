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


