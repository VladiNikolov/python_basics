number = int(input())
sum = 0
count = 0
for first_number in range(0, number + 1):
    for second_number in range(0, number + 1):
        for third_number in range(0, number + 1):
            sum = first_number + second_number + third_number
            if sum == number:
                count += 1
print(count)



