number = int(input())
sum = 0
for i in range(number):
    current_input = int(input())
    sum = sum + current_input
average = sum / number
print(f"{average:.2f}")


