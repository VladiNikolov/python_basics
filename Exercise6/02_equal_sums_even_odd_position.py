first_number = int(input())
second_number = int(input())

for i in range(first_number, second_number + 1):
    current_number = str(i)
    even_sum = 0
    odd_sum = 0
    for j in range(0, len(current_number)):
        digit = int(current_number[j])
        if j % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
    if even_sum == odd_sum:
        print(current_number, end=" ")