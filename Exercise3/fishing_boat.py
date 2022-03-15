budget = int(input())
season = input()
br_fisherman = int(input())

price = 0
if season == 'Spring':
    price = 3000
    if 0 < br_fisherman <= 6:
        price = price * 0.9
    elif br_fisherman <= 11:
        price = price * 0.85
    elif br_fisherman > 11:
        price = price * 0.75
elif season == 'Winter':
    price = 2600
    if 0 < br_fisherman <= 6:
        price = price * 0.9
    elif br_fisherman <= 11:
        price = price * 0.85
    elif br_fisherman > 11:
        price = price * 0.75
elif season == 'Summer':
    price = 4200
    if 0 < br_fisherman <= 6:
        price = price * 0.9
    elif br_fisherman <= 11:
        price = price * 0.85
    elif br_fisherman >= 12:
        price = price * 0.75
elif season == 'Autumn':
    price = 4200
    if 0 < br_fisherman <= 6:
        price = price * 0.9
    elif br_fisherman <= 11:
        price = price * 0.85
    elif br_fisherman >= 12 :
        price = price * 0.75
if season != 'Autumn' and br_fisherman % 2 == 0:
# <- проверка за четно числото if br_fisherman % 2 == 1: <- проверка за нечетно число
        price = price * 0.95
#season == 'Spring' or season == 'Winter' or season == 'Summer': #

difference = abs(budget - price)
if budget >= price:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")
