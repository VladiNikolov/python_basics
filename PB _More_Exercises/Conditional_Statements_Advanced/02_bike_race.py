count_juniors = int(input())
count_seniors = int(input())
route = input()

all_price_juniors = 0
all_price_seniors = 0
all_people = count_juniors + count_seniors
if route == "trail":
    all_price_juniors = count_juniors * 5.50
    all_price_seniors = count_seniors * 7
elif route == "cross-country":
    all_price_juniors = count_juniors * 8
    all_price_seniors = count_seniors * 9.50
    if all_people >= 50:
        all_price_juniors = count_juniors * (8 * 0.75)
        all_price_seniors = count_seniors * (9.50 * 0.75)
elif route == "downhill":
    all_price_juniors = count_juniors * 12.25
    all_price_seniors = count_seniors * 13.75
elif route == "road":
    all_price_juniors = count_juniors * 20
    all_price_seniors = count_seniors * 21.50
total_price = (all_price_seniors + all_price_juniors) * 0.95
print(f"{total_price:.2f}")


