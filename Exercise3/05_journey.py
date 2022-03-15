# •	Бюджет - реално число;
# •	Един от двата възможни сезона - "summer” или "winter”.
budget = float(input())
season = input()
destination = ""
journey = ""
price = 0
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        journey = "Camp"
        price = budget * 0.30
    elif season == "winter":
        journey = "Hotel"
        price = budget * 0.70
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        journey = "Camp"
        price = budget * 0.40
    elif season == "winter":
        journey = "Hotel"
        price = budget * 0.80
elif budget > 1000:
    destination = "Europe"
    journey = "Hotel"
    price = budget * 0.90
print(f"Somewhere in {destination}")
print(f"{journey} - {price:.2f}")
