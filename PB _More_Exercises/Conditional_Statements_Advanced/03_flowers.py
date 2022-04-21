number_chrysanthemum = int(input())
number_roses = int(input())
number_tulips = int(input())
seasons = input()
holiday = input()

price_roses = 0
price_tulips = 0
price_chrysanthemum = 0
all_price = 0
if (seasons == "Spring" or seasons == "Summer") and holiday == "Y":
    price_chrysanthemum = number_chrysanthemum * 2
    price_roses = number_roses * 4.10
    price_tulips = number_tulips * 2.50
    all_price = (price_roses + price_tulips + price_chrysanthemum) * 1.15
    if number_tulips > 7:
        all_price = all_price * 0.95
elif (seasons == "Spring" or seasons == "Summer") and holiday == "N":
    price_chrysanthemum = number_chrysanthemum * 2
    price_roses = number_roses * 4.10
    price_tulips = number_tulips * 2.50
    all_price = price_roses + price_tulips + price_chrysanthemum
    if number_tulips > 7:
        all_price = all_price * 0.95
elif (seasons == "Autumn" or seasons == "Winter") and holiday == "Y":
    price_chrysanthemum = number_chrysanthemum * 3.75
    price_roses = number_roses * 4.50
    price_tulips = number_tulips * 4.15
    all_price = (price_roses + price_tulips + price_chrysanthemum) * 1.15
    if number_roses >= 10:
        price_roses = price_roses * 0.90
elif seasons == "Winter" and holiday == "N":
    price_chrysanthemum = number_chrysanthemum * 3.75
    price_roses = number_roses * 4.50
    price_tulips = number_tulips * 4.15
    all_price = price_roses + price_tulips + price_chrysanthemum
    if number_roses >= 10:
        all_price = all_price * 0.90
elif seasons == "Autumn" and holiday == "N":
    price_chrysanthemum = number_chrysanthemum * 3.75
    price_roses = number_roses * 4.50
    price_tulips = number_tulips * 4.15
    all_price = price_roses + price_tulips + price_chrysanthemum

sum_number_flowers = number_roses + number_tulips + number_chrysanthemum


if sum_number_flowers > 20:
    all_price = (all_price * 0.80) + 2
else:
    all_price = all_price + 2
print(f"{all_price:.2f}")
