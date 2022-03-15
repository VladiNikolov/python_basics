width = int(input())
length = int(input())
height = int(input())
there_is_more_free_space = True
total_volume = width * length * height
command = input()
while command != 'Done':
    number_of_boxes = int(command)
    total_volume -= number_of_boxes # total_volume = total_volume - number_of_boxes
    if total_volume <= 0:
        there_is_more_free_space = False
        break
    command = input()
if there_is_more_free_space: # if total_volume >0
    print(f'{total_volume} Cubic meters left.')
else:
    print(f"No more free space! You need {abs(total_volume)} Cubic meters more.")


