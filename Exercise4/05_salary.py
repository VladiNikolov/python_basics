number_open_tabs = int(input())
salary = int(input())

for i in range(number_open_tabs):
    current_input = input()
    if current_input == "Facebook":
        penalty = 150
        salary = salary - penalty
    elif current_input == "Instagram":
        penalty = 100
        salary = salary - penalty
    elif current_input == "Reddit":
        penalty = 50
        salary = salary - penalty
    if salary <= 0:
        break
if salary <= 0:
    print("You have lost your salary.")
else:
    print(f"{salary}")


