x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
x = float(input())
y = float(input())

first_case = (x == x_1 or x == x_2) and (y >= y_1 and y <= y_2)
second_case = (y == y_1 or y == y_2) and (x >= x_1 and x <= x_2)
if first_case or second_case:
    print("Border")
else:
    print("Inside / Outside")