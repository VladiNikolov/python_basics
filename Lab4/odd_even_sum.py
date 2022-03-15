n = int(input())

even_sum = 0
odd_sum = 0
for i in range (1, n + 1):
    current_num = int(input())

    if i % 2 == 0:
        even_sum += current_num
    else:
        odd_sum += current_num

if even_sum == odd_sum:
    print('Yes')
    print(f'Sum = {even_sum}')
else:
    print('No')
    diff = abs(even_sum - odd_sum)
    print(f'Diff = {diff}')