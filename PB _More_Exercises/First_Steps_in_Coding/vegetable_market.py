price_vegetable = float(input())
price_fruit = float(input())
kilogram_vegetable = int(input())
kilogram_fruit = int(input())

all_price_vegetable = price_vegetable * kilogram_vegetable
all_price_fruit = price_fruit * kilogram_fruit

total_price = (all_price_vegetable + all_price_fruit) / 1.94
print(f'{total_price:.2f}')