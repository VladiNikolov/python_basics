command = input()
all_sum = 0

while command != "NoMoreMoney":
    current_sum = float(command)
    if current_sum < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {current_sum:.2f}")
    all_sum += current_sum

    command = input()
print(f"Total: {all_sum:.2f}")

