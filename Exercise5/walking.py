needed_steps = 10000
total_steps = 0
while total_steps < needed_steps:
    command = input()
    if command == 'Going home':
        last_steps = int(input())
        total_steps = total_steps + last_steps
        break
    current_steps = int(command)
    total_steps = total_steps + current_steps
difference = abs(total_steps - needed_steps)
if total_steps >= needed_steps:
    print(f'Goal reached! Good job!')
    print(f'{difference} steps over the goal!')
else:
    print(f'{difference} more steps to reach goal.')




