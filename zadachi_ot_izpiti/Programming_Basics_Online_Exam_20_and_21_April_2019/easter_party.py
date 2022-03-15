guest = int(input())
price_kuvert = float(input())
budget = float(input())
price_cake = 0
if guest < 10:
    price_kuvert = price_kuvert
elif 10 <= guest <= 15:
    price_kuvert = price_kuvert * 0.85
elif guest <= 20:
    price_kuvert = price_kuvert * 0.80
elif guest > 20:
    price_kuvert = price_kuvert * 0.75
price_cake = budget * 0.1
all_price = (price_kuvert * guest) + price_cake
#total = all_price - price_cake
difference = abs(budget - all_price)
if budget > all_price:
    print(f"It is party time! {difference:.2f} leva left.")
else:
    print(f"No party! {difference:.2f} leva needed.")


