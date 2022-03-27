number = int(input())
p_1 = 0
p_2 = 0
p_3 = 0
p_4 = 0
p_5 = 0
all_numbers = 0
for number in range(1, number + 1):
    current_number = int(input())
    if current_number < 200:
        p_1 += 1
    elif current_number <= 399:
        p_2 += 1
    elif current_number <= 599:
        p_3 += 1
    elif current_number <= 799:
        p_4 += 1
    elif current_number >= 800:
        p_5 += 1
all_numbers = p_1 + p_2 + p_3 + p_4 + p_5

print(f"{(p_1 / all_numbers)*100:.2f}%")
print(f"{(p_2 / all_numbers)*100:.2f}%")
print(f"{(p_3 / all_numbers)*100:.2f}%")
print(f"{(p_4 / all_numbers)*100:.2f}%")
print(f"{(p_5 / all_numbers)*100:.2f}%")
