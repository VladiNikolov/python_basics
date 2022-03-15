days = int(input())
type_of_room = input()
rating = input()

price = 0
all_price = 0
if type_of_room == "room for one person":
    price = 18
    days = days - 1
    all_price = price * days
elif type_of_room == "apartment":
    price = 25
    if days < 10:
        days = days - 1
        all_price = (price * days) * 0.70
    elif 10 <= days <= 15:
        days = days - 1
        all_price = (price * days) * 0.65
    elif days > 15:
        days = days - 1
        all_price = (price * days) / 2
elif type_of_room == "president apartment":
    price = 35
    if days < 10:
        days = days - 1
        all_price = (price * days) * 0.90
    elif 10 <= days <= 15:
        days = days - 1
        all_price = (price * days) * 0.85
    elif days > 15:
        days = days - 1
        all_price = (price * days) * 0.80
if rating == "positive":
    all_price = all_price * 1.25
elif rating == "negative":
    all_price = all_price * 0.90
print(f"{all_price:.2f}")