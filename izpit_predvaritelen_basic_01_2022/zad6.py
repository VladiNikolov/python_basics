number = int(input())
reach = False
count = 0

for a in range(1, 9 +1):
    for b in range(9, a, -1):
        for c in range(0, 9 +1):
            for d in range(9, c, -1):
                sum = a+b+c+d
                prod = a*b*c*d
                if sum == prod and number % 10 == 5:
                    count +=1
                    print(f"{a}{b}{c}{d}")
                    reach = True
                    break
                elif prod // sum == 3 and number % 3 == 0:
                    count +=1
                    print(f"{d}{c}{b}{a}")
                    reach = True
                    break
            if reach:
                break
        if reach:
            break
    if reach:
        break
if count == 0:
    print("Nothing found")


