# •	Бюджетът, с който разполагат – реално число в интервала [1.00 … 10000.00]
# •	Брой нощувки – цяло число в интервала [0 … 1000]
# •	Цена за нощувка – реално число в интервала [1.00 … 500.00]
# •	Процент за допълнителни разходи – цяло число в интервала [0 … 100]
budget = float(input())
number_of_sleeps = int(input())
price_for_sleep = float(input())
prcents = int(input())
all_night_price = 0
costs = (budget * prcents) / 100
if number_of_sleeps <= 7:
    all_night_price = (number_of_sleeps * price_for_sleep) + costs
elif number_of_sleeps > 7:
    all_night_price = number_of_sleeps * price_for_sleep
    all_night_price = all_night_price * 0.95
    all_night_price = all_night_price + costs

difference = abs(budget - all_night_price)

if budget >= all_night_price:
    print(f"Ivanovi will be left with {difference:.2f} leva after vacation.")
else:
    print(f"{difference:.2f} leva needed.")

