budget = int(input())
season = input()
count_fisherman = int(input())

price_boat = 0
if season == "Spring":
    price_boat = 3000
    if count_fisherman <= 6:
        price_boat = price_boat * 0.90
    elif count_fisherman <= 11:
        price_boat = price_boat * 0.85
    elif count_fisherman > 12:
        price_boat = price_boat * 0.75
elif season == "Summer" or season == "Autumn":
    price_boat = 4200
    if count_fisherman <= 6:
        price_boat = price_boat * 0.90
    elif count_fisherman <= 11:
        price_boat = price_boat * 0.85
    elif count_fisherman > 12:
        price_boat = price_boat * 0.75
elif season == "Winter":
    price_boat = 2600
    if count_fisherman <= 6:
        price_boat = price_boat * 0.90
    elif count_fisherman <= 11:
        price_boat = price_boat * 0.85
    elif count_fisherman > 12:
        price_boat = price_boat * 0.75
if count_fisherman % 2 == 0 and (season == "Spring" or season == "Summer" or season == "Winter"):
    price_boat = price_boat * 0.95
difference = abs(budget - price_boat)
if budget >= price_boat:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")
