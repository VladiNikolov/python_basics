flowers = input()
br_flowers = int(input())
budget = int(input())

price = 0
if flowers == 'Roses':
    price = 5
    if br_flowers > 80:
        price = price * 0.9
elif flowers == 'Dahlias':
    price = 3.80
    if br_flowers > 90:
        price = price * 0.85
elif flowers == 'Tulips':
    price = 2.80
    if br_flowers > 80:
        price = price * 0.85
elif flowers == 'Narcissus':
    price = 3
    if br_flowers < 120:
        price = price * 1.15
elif flowers == 'Gladiolus':
    price = 2.50
    if br_flowers < 80:
        price = price * 1.20
total_price = price * br_flowers
differents = abs(budget - total_price)
if budget >= total_price:
    print(f"Hey, you have a great garden with {br_flowers} {flowers} and {differents:.2f} leva left.")
else:
    print(f"Not enough money, you need {differents:.2f} leva more.")




