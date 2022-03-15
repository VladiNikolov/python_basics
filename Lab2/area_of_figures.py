import math

figure = input()

side_a = float(input())

#area = 0
if figure == 'square':
    area = side_a * side_a
    print(f'{area:.3f}')
elif figure == 'rectangle':
    side_b = float(input())
    area = side_a * side_b
    print(f'{area:.3f}')
elif figure == 'circle':
    area = math.pi * side_a * side_a
    print(f'{area:.3f}')
elif figure == 'triangle':
    h = float(input())
    area = (side_a * h) / 2
    print(f'{area:.3f}')