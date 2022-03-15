width = int(input())
lenght = int(input())
size_of_cake = width * lenght
there_is_more_pieses_cake = True
command = int(input())
while command != 'STOP':
    piece_of_cake = int(command)
    size_of_cake = size_of_cake - piece_of_cake
    if size_of_cake < 0:
        there_is_more_pieses_cake = False
        break
    command = input()
if there_is_more_pieses_cake:
    print(f"{size_of_cake} pieces are left.")
else:
    print(f"No more cake left! You need {abs(size_of_cake)} pieces more.")



