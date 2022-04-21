number = int(input())
star = "*"
interval = " "

for row in range(1, number+1):
    num1 = number - row
    num2 = row - 1
    print(f"{interval}" * num1 + star + " " + f"{star} " * num2)
for row in range(number - 1, 0, -1):
    num1 = number - row
    num2 = row - 1
    print(f"{interval}" * num1 + star + " " + f"{star} " * num2)


   # print(f"{interval}" * num1 + star + " " + f"{star}" * num2)
