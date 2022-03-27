count_of_numbers = int(input())
odd_sum = 0
even_sum = 0

for position in range(1, count_of_numbers + 1):
    current_number = int(input())
    if position % 2 == 0:
        even_sum = even_sum + current_number
    else:
        odd_sum = odd_sum + current_number
difference = abs(even_sum - odd_sum)
if even_sum == odd_sum:
    print("Yes")
    print(f"Sum = {even_sum}")
else:
    print("No")
    print(f"Diff = {difference}")