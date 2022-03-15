first_number = int(input())
second_number = int(input())

for current_number in range(first_number, second_number + 1):
    odd_digits_sum = 0
    even_digits_sum = 0
    current_number_as_string = str(current_number)
    for index, digit in enumerate(current_number_as_string):
        if index % 2 == 0:
            odd_digits_sum += int(digit)
        else:
            even_digits_sum += int(digit)
    if odd_digits_sum == even_digits_sum:
        print(current_number_as_string, end=" ")
