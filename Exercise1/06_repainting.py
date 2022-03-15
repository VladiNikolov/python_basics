nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

all_nylon = (2 + nylon) * 1.50
all_paint = (paint * 14.50) * 1.1
all_thinner = thinner * 5
sum_total = all_nylon + all_paint + all_thinner + 0.40
all_sum = (sum_total * 0.30) * hours
total = all_sum + sum_total
print(f"{total}")