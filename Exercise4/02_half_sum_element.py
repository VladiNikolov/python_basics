import sys

n = int(input())

sum = 0
max_number = - sys.maxsize
for i in range(1, n + 1):
    current_number = int(input())
    sum = sum + current_number #sum += current_number
    if current_number > max_number:
        max_number = current_number
sum = sum - max_number
if sum == max_number:
    print("Yes")
    print(f"Sum = {sum}")
else:
    print("No")
    print(f"Diff = {abs(sum - max_number)}")
