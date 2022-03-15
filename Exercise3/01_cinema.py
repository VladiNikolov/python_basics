projections = input()
rows = int(input())
columns = int(input())

all_price = 0
if projections == "Premiere":
    price = 12
    all_place = rows * columns
    all_price = all_place * price
elif projections == "Normal":
    price = 7.50
    all_place = rows * columns
    all_price = all_place * price
elif projections == "Discount":
    price = 5
    all_place = rows * columns
    all_price = all_place * price
print(f"{all_price:.2f} leva")
