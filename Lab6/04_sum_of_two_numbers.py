start_number = int(input())
end_number = int(input())
magic_number = int(input())
sum = 0
count = 0
is_combination_found = False
for first_number in range(start_number, end_number + 1):
    for second_number in range(start_number, end_number + 1):
        sum = first_number + second_number
        count += 1
        if sum == magic_number:
            print(f"Combination N:{count} ({first_number} + {second_number} = {sum})")
            is_combination_found = True
            break
    if is_combination_found:
        break
if not is_combination_found:
    print(f"{count} combinations - neither equals {magic_number}")

