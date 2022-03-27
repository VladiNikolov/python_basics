age_lily = int(input())
price_laundry = float(input())
price_toys = int(input())
all_sum = 0
count_toys = 0

for i in range(1, age_lily + 1):
    if i % 2 == 0:
        all_sum = all_sum + (i / 2) * 10
        all_sum = all_sum - 1
    else:
        count_toys = count_toys + 1
all_price_toys = (count_toys * price_toys) + all_sum
difference = abs(price_laundry - all_price_toys)
if all_price_toys >= price_laundry:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")


