# •	Брой магнолии – цяло число в интервала [0 … 50]
# •	Брой зюмбюли – цяло число в интервала [0 … 50]
# •	Брой рози – цяло число в интервала [0 … 50]
# •	Брой кактуси – цяло число в интервала [0 … 50]
# •	Цена на подаръка – реално число в интервала [0.00 … 500.00]
import math
number_magnolias = int(input())
number_hyacinths = int(input())
number_roses = int(input())
number_cactus = int(input())
price_gift = float(input())

magnolias_price = number_magnolias * 3.25
hyacinths_price = number_hyacinths * 4
roses_price = number_roses * 3.50
cactus_price = number_cactus * 8

all_price_flowers = (magnolias_price + hyacinths_price + roses_price + cactus_price) * 0.95
difference = abs(price_gift - all_price_flowers)
if all_price_flowers >= price_gift:
    print(f"She is left with {math.floor(difference)} leva.")
else:
    print(f"She will have to borrow {math.ceil(difference)} leva.")