# width_of_cake = int(input())
# length_of_cake = int(input())
# all_size_cake = width_of_cake * length_of_cake
# more_piese_cake = True
# command = input()
# count_piece = 0
# while command != "STOP":
#     current_input = int(command)
#     count_piece += current_input
#     all_size_cake = all_size_cake - current_input
#
#     if all_size_cake < 0:
#         more_piese_cake = False
#         break
#     command = input()
# difference = abs(all_size_cake - count_piece)
# if more_piese_cake:
#     print(f"{all_size_cake} pieces are left.")
# else:
#     print(f"No more cake left! You need {abs(all_size_cake)} pieces more.")
#

width_of_cake = int(input())
length_of_cake = int(input())
all_size_cake = width_of_cake * length_of_cake
more_piese_cake = True
command = input()
count_piece = 0
for i in range(all_size_cake):
    if command == "STOP":
        more_piese_cake = True
        break
    current_input = int(command)
    count_piece += current_input

    all_size_cake = all_size_cake - current_input

    if all_size_cake < 0:
        more_piese_cake = False
        break
    command = input()
difference = abs(all_size_cake - count_piece)
if more_piese_cake:
    print(f"{all_size_cake} pieces are left.")
else:
    print(f"No more cake left! You need {abs(all_size_cake)} pieces more.")



