number = int(input())

current_number = 1
is_bigger_then_number = False
for row in range(1, 10 + 1):
    for collum in range(1, row + 1):
        if current_number > number:
            is_bigger_then_number = True
            break
        print(current_number, end= " ")
        current_number += 1
    if is_bigger_then_number:
        break
    print()
