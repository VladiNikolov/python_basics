number = int(input())

sum = 0
for i in range(number):
    current_number = int(input())
    sum = current_number + sum
print(f'{sum/number:.2f}')
