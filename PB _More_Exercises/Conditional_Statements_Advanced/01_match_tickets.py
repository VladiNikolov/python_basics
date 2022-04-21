budget = float(input())
category = input()
count_people = int(input())
price = 0

if category == "VIP":
    price = 499.99
    if 1 <= count_people <= 4:
        budget = budget * 0.25
    elif count_people <= 9:
        budget = budget * 0.40
    elif count_people <= 24:
        budget = budget * 0.50
    elif count_people <= 49:
        budget = budget * 0.60
    elif count_people >= 50:
        budget = budget * 0.75
if category == "Normal":
    price = 249.99
    if 1 <= count_people <= 4:
        budget = budget * 0.25
    elif count_people <= 9:
        budget = budget * 0.40
    elif count_people <= 24:
        budget = budget * 0.50
    elif count_people <= 49:
        budget = budget * 0.60
    elif count_people >= 50:
        budget = budget * 0.75
all_price_tickets = count_people * price
difference = abs(budget - all_price_tickets)
if budget >= all_price_tickets:
    print(f"Yes! You have {difference:.2f} leva left.")

else:
    print(f"Not enough money! You need {difference:.2f} leva.")