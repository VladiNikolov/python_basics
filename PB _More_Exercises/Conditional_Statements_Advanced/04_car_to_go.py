budget = float(input())
season = input()

type_of_class = ""
type_of_car = ""
price_car = 0

if budget <= 100:
    type_of_class = "Economy class"
    if season == "Summer":
        type_of_car = "Cabrio"
        price_car = budget * 0.35
    elif season == "Winter":
        type_of_car = "Jeep"
        price_car = budget * 0.65
elif budget <= 500:
    type_of_class = "Compact class"
    if season == "Summer":
        type_of_car = "Cabrio"
        price_car = budget * 0.45
    elif season == "Winter":
        type_of_car = "Jeep"
        price_car = budget * 0.80
elif budget > 500:
    type_of_class = "Luxury class"
    type_of_car = "Jeep"
    price_car = budget * 0.90
print(f"{type_of_class}")
print(f"{type_of_car} - {price_car:.2f}")





