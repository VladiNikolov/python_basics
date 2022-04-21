number = int(input())
current_number = int(input())
sum = 0

while sum != number:
    sum += current_number
    if sum >= number:
        break
    current_number = int(input())
print(sum)
