price_excursion = float(input())
number_puzzles = int(input())
number_dolls = int(input())
number_teddy_bears = int(input())
number_minions = int(input())
number_trucks = int(input())

price_puzzle = 2.60
price_dolls = 3
price_teddy_bear = 4.10
price_minions = 8.20
price_truck = 2

all_number_toy = number_trucks + number_dolls + number_minions + number_puzzles + number_teddy_bears

total_price = (price_truck * number_trucks) + (price_puzzle * number_puzzles) +\
              (price_minions * number_minions) + (price_dolls * number_dolls) + (price_teddy_bear * number_teddy_bears)
total_price = total_price * 0.90

if all_number_toy >= 50:
    total_price = total_price * 0.75
difference = abs(price_excursion - total_price)
if total_price >= price_excursion:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")