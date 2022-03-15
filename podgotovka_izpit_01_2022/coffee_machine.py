beverage = input()
sugar = input()
number_of_beverages = int(input())

all_price = 0

if beverage == "Espresso":
    if sugar == "Without":
        price = 0.90
        all_price = (price * number_of_beverages) * 0.65
        if number_of_beverages >= 5:
            all_price = all_price * 0.75
    elif sugar == "Normal":
        price = 1.00
        all_price = price * number_of_beverages
        if number_of_beverages >= 5:
            all_price = all_price * 0.75
    elif sugar == "Extra":
        price = 1.20
        all_price = price * number_of_beverages
        if number_of_beverages >= 5:
            all_price = all_price * 0.75
elif beverage == "Cappuccino":
    if sugar == "Without":
        price = 1.00
        all_price = (price * number_of_beverages) * 0.65
    elif sugar == "Normal":
        price = 1.20
        all_price = price * number_of_beverages
    elif sugar == "Extra":
        price = 1.60
        all_price = price * number_of_beverages
elif beverage == "Tea":
    if sugar == "Without":
        price = 0.50
        all_price = (price * number_of_beverages) * 0.65
    elif sugar == "Normal":
        price = 0.60
        all_price = price * number_of_beverages
    elif sugar == "Extra":
        price = 0.70
        all_price = price * number_of_beverages
if all_price > 15:
    all_price = all_price * 0.80
print(f"You bought {number_of_beverages} cups of {beverage} for {all_price:.2f} lv.")

