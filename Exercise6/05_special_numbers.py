number = int(input())

for i in range(1, 9 + 1):
    for j in range(1, 9 + 1):
        for k in range(1, 9 + 1):
            for l in range(1, 9 + 1):
                if number % i == 0 and number % j == 0 and number % k == 0 and number % l == 0:
                    print(f"{i}{j}{k}{l}", end=" ")
