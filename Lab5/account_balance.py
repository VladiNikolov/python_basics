input_line = input()

balance = 0
while input_line != 'NoMoreMoney':
    sum = float(input_line)
    if sum < 0:
        print('Invalid operation!')
        break
    balance = balance + sum
    print(f'Increase: {sum:.2f}')

    input_line = input()
print(f'Total: {balance:.2f}')