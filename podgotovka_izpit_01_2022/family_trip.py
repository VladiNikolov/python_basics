budget = float(input())
number_of_sleeps = int(input())
price_sleeps = float(input())
percentage_costs = int(input())
total_price = 0

all_percentage_costs = budget * percentage_costs / 100
if number_of_sleeps > 7:
     price_sleeps = price_sleeps * 0.95
     price_all_sleeps = number_of_sleeps * price_sleeps
     total_price = price_all_sleeps + all_percentage_costs
elif 0 < number_of_sleeps <= 7:
     price_all_sleeps = price_sleeps * number_of_sleeps
     total_price = price_all_sleeps + all_percentage_costs
difference = abs(budget - total_price)
if budget >= total_price:
     print(f"Ivanovi will be left with {difference:.2f} leva after vacation.")
else:
     print(f"{difference:.2f} leva needed.")

