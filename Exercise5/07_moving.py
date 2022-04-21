# width = int(input())
# length = int(input())
# height = int(input())
# all_space = width * length * height
# is_full = False
# count_box = 0
# command = input()
# while command != "Done":
#     current_input = int(command)
#     all_space -= current_input
#     if all_space <= 0:
#         is_full = True
#         break
#     command = input()
# if is_full:
#     print(f"No more free space! You need {abs(all_space)} Cubic meters more.")
# else:
#     print(f"{all_space} Cubic meters left.")

width = int(input())
length = int(input())
height = int(input())
all_space = width * length * height
is_full = False
count_box = 0
command = input()
for i in range(all_space):
    if command == "Done":
        is_full = False
        break
    current_input = int(command)
    all_space -= current_input
    if all_space <= 0:
        is_full = True
        break
    command = input()
if is_full:
    print(f"No more free space! You need {abs(all_space)} Cubic meters more.")
else:
    print(f"{all_space} Cubic meters left.")