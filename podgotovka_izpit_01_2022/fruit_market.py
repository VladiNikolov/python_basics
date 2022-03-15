# 1.	Цена на ягодите в лева – реално число в интервала [0.00 … 10000.00]
# 2.	Количество на бананите в килограми – реално число в интервала [0.00 … 1 0000.00]
# 3.	Количество на портокалите в килограми – реално число в интервала [0.00 … 10000.00]
# 4.	Количество на малините в килограми – реално число в интервала [0.00 … 10000.00]
# 5.	Количество на ягодите в килограми – реално число в интервала [0.00 … 10000.00]


price_berries = float(input())
bananas = float(input())
orange = float(input())
raspberries = float(input())
berries = float(input())

price_raspberries = price_berries * 0.50
price_orange = price_raspberries * 0.60
price_babanas = price_raspberries * 0.20

total_price_berries = price_berries * berries
total_price_bananas = price_babanas * bananas
total_price_orange = price_orange * orange
total_price_raspberries = price_raspberries * raspberries

all_sum = total_price_berries + total_price_orange + total_price_bananas + total_price_raspberries
print(f"{all_sum:.2f}")