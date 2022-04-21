number = int(input())

for row in range(number):
    for column in range(row + 1):
        print(f"$", end=" ")
    print()