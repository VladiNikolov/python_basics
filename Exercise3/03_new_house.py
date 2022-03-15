name_flowers = input()
count_flowers = int(input())
budget = int(input())

price_roses = 5
price_dahlias = 3.80
price_tulips = 2.80
price_narcissus = 3
price_gladiolus = 2.50
all_price = 0
if name_flowers == "Roses":
    all_price = price_roses * count_flowers
    if count_flowers > 80:
        all_price = (price_roses * count_flowers) * 0.90
elif name_flowers == "Dahlias":
    all_price = price_dahlias * count_flowers
    if count_flowers > 90:
        all_price = (price_dahlias * count_flowers) * 0.85
elif name_flowers == "Tulips":
    all_price = price_tulips * count_flowers
    if count_flowers > 80:
        all_price = (price_tulips * count_flowers) * 0.85
elif name_flowers == "Narcissus":
    all_price = price_narcissus * count_flowers
    if count_flowers < 120:
        all_price = (price_narcissus * count_flowers) * 1.15
elif name_flowers == "Gladiolus":
    all_price = price_gladiolus * count_flowers
    if count_flowers < 80:
        all_price = (price_gladiolus * count_flowers) * 1.2
difference = abs(budget - all_price)
if budget >= all_price:
    print(f"Hey, you have a great garden with {count_flowers} {name_flowers} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")