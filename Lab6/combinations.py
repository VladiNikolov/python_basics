n = int(input())

count = 0
for x1 in range(n+1):
    for x2 in range(n+1):
        for x3 in range(n+1):
            sum = x1 + x2 +x3

            if sum == n:
                count += 1
print(count)
