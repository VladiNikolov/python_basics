seasons = input()
kilometers_per_month = float(input())
price_per_one_kilometer = 0

if seasons == "Spring" or seasons == "Autumn":
    if kilometers_per_month <= 5000:
        price_per_one_kilometer = 0.75
    elif kilometers_per_month <= 10000:
        price_per_one_kilometer = 0.95
    elif kilometers_per_month <= 20000:
        price_per_one_kilometer = 1.45
elif seasons == "Winter":
    if kilometers_per_month <= 5000:
        price_per_one_kilometer = 1.05
    elif kilometers_per_month <= 10000:
        price_per_one_kilometer = 1.25
    elif kilometers_per_month <= 20000:
        price_per_one_kilometer = 1.45
elif seasons == "Summer":
    if kilometers_per_month <= 5000:
        price_per_one_kilometer = 0.90
    elif kilometers_per_month <= 10000:
        price_per_one_kilometer = 1.10
    elif kilometers_per_month <= 20000:
        price_per_one_kilometer = 1.45
all_price = (price_per_one_kilometer * kilometers_per_month * 4) * 0.90
print(f"{all_price:.2f}")


