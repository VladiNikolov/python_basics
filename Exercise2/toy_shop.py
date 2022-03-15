price_excursion = float(input())
puzzle = int(input())
talking_doll = int(input())
teddy_bear = int(input())
minions = int(input())
trucks = int(input())

total_price_puzzle = puzzle * 2.60
total_price_talking_doll = talking_doll * 3
total_price_teddy_bear = teddy_bear * 4.10
total_price_minions = minions * 8.20
total_price_truck = trucks * 2

all_price_order = total_price_puzzle + total_price_talking_doll + \
                  total_price_teddy_bear + total_price_minions + total_price_truck  #общо пари от всички играчки
count_toy = puzzle + talking_doll + teddy_bear + minions + trucks  #общо бройки играчки

if count_toy >= 50:
    all_price_order = all_price_order * 0.75

total_price = all_price_order * 0.90  # 10 процента наем

differens = abs(total_price - price_excursion) #цяла печалба минус цена на екскурзията

if price_excursion <= total_price:
    print(f'Yes! {differens:.2f} lv left.')
else:
    print(f'Not enough money! {differens:.2f} lv needed.')
