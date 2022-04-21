needed_steps = 10000
all_steps = 0
while all_steps < needed_steps:
    command = input()
    if command == "Going home":
        input_last_step = int(input())
        all_steps += input_last_step
        break
    current_steps = int(command)
    all_steps += current_steps
difference = abs(needed_steps - all_steps)
if all_steps > needed_steps:
    print("Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
else:
    print(f"{difference} more steps to reach goal.")


