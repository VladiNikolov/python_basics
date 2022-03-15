# •	Първи ред – Цена за килограм зеленчуци – реално число[0.00… 1000.00]
# •	Втори ред – Цена за килограм плодове – реално число[0.00… 1000.00]
# •	Трети ред – Общо килограми на зеленчуците – цяло число[0… 1000]
# •	Четвърти ред – Общо килограми на плодовете – цяло число[0… 1000]

price_vegetable = float(input())
price_fruit = float(input())
total_kilogram_vegetable = int(input())
total_kilogram_fruit = int(input())
euro = 1.94

total_sum_vegetable = price_vegetable * total_kilogram_vegetable
total_sum_fruit = price_fruit * total_kilogram_fruit
all_sum = total_sum_fruit + total_sum_vegetable
all_sum_euro = all_sum / euro
print(f"{all_sum_euro:.2f}")
