number = int(input())
interval = " "
star = "*"
for row in range(1, number+2):
    print(f"{interval}" * (number - row+1) + star * (row-1) + " | " + star * (row-1))