import sys

number = int(input())
current_result = 0
old_result = -sys.maxsize
difference = 0
maxdiff = 0
for i in range(1, number + 1):
    current_number_a = int(input())
    current_number_b = int(input())
    current_result = current_number_a + current_number_b
    if old_result == -sys.maxsize:
        old_result = current_result
    if current_result != old_result:
        difference = abs(old_result - current_result)
        if maxdiff < difference:
            maxdiff = difference
    old_result = current_result
if maxdiff == 0:
    print(f"Yes, value={old_result}")
else:
    print(f"No, maxdiff={maxdiff}")



