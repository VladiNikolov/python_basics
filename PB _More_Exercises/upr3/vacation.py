budget = float(input())
season = input()
location = ""
accommodation = ""
price = 0

if budget <= 1000:
    accommodation = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = 0.65
    elif season == "Winter":
        location = "Morocco"
        price = 0.45
elif budget <= 3000:
    accommodation = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = 0.80
    elif season == "Winter":
        location = "Morocco"
        price = 0.60
elif budget > 3000:
    accommodation = "Hotel"
    if season == "Summer":
        location = "Alaska"
        price = 0.90
    elif season == "Winter":
        location = "Morocco"
        price = 0.90
all_price = budget * price
print(f"{location} - {accommodation} - {all_price:.2f}")

