budget = float(input())
number_videocards = int(input())
number_procesors = int(input())
number_ram_memory = int(input())

price_videocard = number_videocards * 250
price_procesor = (price_videocard * 0.35) * number_procesors
price_ram_memory = (price_videocard * 0.10) * number_ram_memory
all_price = price_procesor + price_ram_memory + price_videocard

if number_videocards > number_procesors:
    all_price = all_price * 0.85
difference = abs(budget - all_price)
if budget >= all_price:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")