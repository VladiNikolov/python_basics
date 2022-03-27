number_juniors = int(input())
number_seniors = int(input())
route = input()
price_juniors = 0
price_seniors = 0
all_price = 0
sum_players = number_seniors + number_juniors
if route == "trail":
    price_juniors = price_juniors + (number_juniors * 5.5)
    price_seniors = price_seniors + (number_seniors * 7)
    all_price = price_juniors + price_seniors
elif route == "cross-country":
    if sum_players >= 50:
        price_juniors = price_juniors + (number_juniors * 8)
        price_seniors = price_seniors + (number_seniors * 9.50)
        all_price = (price_juniors + price_seniors) * 0.75
    elif 0 < sum_players < 49:
        price_juniors = price_juniors + (number_juniors * 8)
        price_seniors = price_seniors + (number_seniors * 9.50)
        all_price = price_juniors + price_seniors
elif route == "downhill":
    price_juniors = price_juniors + (number_juniors * 12.25)
    price_seniors = price_seniors + (number_seniors * 13.75)
    all_price = price_juniors + price_seniors
elif route == "road":
    price_juniors = price_juniors + (number_juniors * 20)
    price_seniors = price_seniors + (number_seniors * 21.50)
    all_price = price_juniors + price_seniors
total_price = all_price * 0.95
print(f"{total_price:.2f}")

