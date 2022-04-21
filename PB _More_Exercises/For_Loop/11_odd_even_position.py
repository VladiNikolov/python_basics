import sys

number = int(input())
odd_sum = 0.00
odd_min = sys.maxsize
odd_max = -sys.maxsize
even_sum = 0.00
even_min = sys.maxsize
even_max = -sys.maxsize

for num in range(1, number + 1):
    current_num = float(input())
    if num % 2 != 0:
        odd_sum += current_num
        if current_num > odd_max:
            odd_max = current_num
        if current_num < odd_min:
            odd_min = current_num
    else:
        even_sum += current_num
        if current_num > even_max:
            even_max = current_num
        if current_num < even_min:
            even_min = current_num
print(f"OddSum={odd_sum:.2f},")
if odd_min == sys.maxsize:
    is_odd_min = "No"
    print(f"OddMin={is_odd_min},")
else:
    is_odd_min = odd_min
    print(f"OddMin={is_odd_min:.2f},")
if odd_max == -sys.maxsize:
    is_odd_max = "No"
    print(f"OddMax={is_odd_max},")
else:
    is_odd_max = odd_max
    print(f"OddMax={is_odd_max:.2f},")
print(f"EvenSum={even_sum:.2f},")
if even_min == sys.maxsize:
    is_even_min = "No"
    print(f"EvenMin={is_even_min},")
else:
    is_even_min = even_min
    print(f"EvenMin={is_even_min:.2f},")
if even_max == -sys.maxsize:
    is_even_max = "No"
    print(f"EvenMax={is_even_max}")
else:
    is_even_max = even_max
    print(f"EvenMax={is_even_max:.2f}")
