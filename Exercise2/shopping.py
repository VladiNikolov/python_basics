budget = float(input())
br_videocards = int(input())
br_procesors = int(input())
br_ram = int(input())

price_videocards = br_videocards * 250
price_procesors = (price_videocards * 0.35) * br_procesors
price_ram = (price_videocards * 0.10) * br_ram

all_price = price_videocards + price_procesors + price_ram

if br_videocards > br_procesors:
    all_price = all_price * 0.85

difference = abs(budget - all_price)
if budget >= all_price:
    print(f'You have {difference:.2f} leva left!')
else:
    print(f'Not enough money! You need {difference:.2f} leva more!')
