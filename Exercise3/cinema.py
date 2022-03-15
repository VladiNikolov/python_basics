tupe_cinema = input()
rows = int(input())
columns = int(input())

price = 0
all_chear = rows * columns
if tupe_cinema == 'Premiere':
    price = 12
elif tupe_cinema == 'Normal':
    price = 7.5
elif tupe_cinema == 'Discount':
    price = 5
print(f'{all_chear * price:.2f} leva')
