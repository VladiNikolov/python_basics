moves = int(input())
sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
sum5 = 0
sum6 = 0
points = 0
for i in range(moves):
    current_number = int(input())
    if current_number < 0:
        points = points / 2
        sum6 += 1
    elif 0 <= current_number <= 9:
        points = points + current_number * 0.20
        sum1 += 1
    elif current_number <= 19:
        points = points + current_number * 0.30
        sum2 += 1
    elif current_number <= 29:
        points = points + current_number * 0.40
        sum3 += 1
    elif current_number <= 39:
        points = points + 50
        sum4 += 1
    elif current_number <= 50:
        points = points + 100
        sum5 += 1
    else:
        points = points / 2
        sum6 += 1
print(f'{points:.2f}')
print(f'From 0 to 9: {sum1 / moves * 100:.2f}%')
print(f'From 10 to 19: {sum2 / moves * 100:.2f}%')
print(f'From 20 to 29: {sum3 / moves * 100:.2f}%')
print(f'From 30 to 39: {sum4 / moves * 100:.2f}%')
print(f'From 40 to 50: {sum5 / moves * 100:.2f}%')
print(f'Invalid numbers: {sum6 / moves * 100:.2f}%')


