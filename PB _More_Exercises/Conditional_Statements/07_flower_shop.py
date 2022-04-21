from math import floor, ceil
count_magnolias = int(input())
count_hyacinths = int(input())
count_rose = int(input())
count_cactus = int(input())
price_gift = float(input())

price_magnolias = 3.25
price_hyacinths = 4
price_rose = 3.50
price_cactus = 8

all_price_magnolias = count_magnolias * 3.25
all_price_hyacinths = count_hyacinths * 4
all_price_rose = count_rose * 3.50
all_price_cactus = count_cactus * 8
total_prise = all_price_cactus + all_price_rose + all_price_hyacinths + all_price_magnolias
total_prise = total_prise * 0.95
difference = abs(price_gift - total_prise)
if price_gift <= total_prise:
    print(f"She is left with {floor(difference)} leva.")
else:
    print(f"She will have to borrow {ceil(difference)} leva.")