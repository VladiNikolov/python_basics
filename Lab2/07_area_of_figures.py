# #import math
# from math import pi
#
# figures = input()
#
# if figures == "square":
#     side_a = float(input())
#     area = side_a * side_a
#     print(f"{area:.3f}")
# elif figures == "rectangle":
#     side_a = float(input())
#     side_b = float(input())
#     area = side_a * side_b
#     print(f"{area:.3f}")
# elif figures == "circle":
#     radius = float(input())
#     area = pi * radius * radius  #area = math.pi * radius* radius
#     print(f"{area:.3f}")
# elif figures == "triangle":
#     side_a = float(input())
#     height_h = float(input())
#     area = (side_a * height_h) / 2
#     print(f"{area:.3f}")

#import math
from math import pi

figures = input()

area = 0
if figures == "square":
    side_a = float(input())
    area = side_a * side_a
elif figures == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
elif figures == "circle":
    radius = float(input())
    area = pi * radius * radius  #area = math.pi * radius* radius
elif figures == "triangle":
    side_a = float(input())
    height_h = float(input())
    area = (side_a * height_h) / 2
print(f"{area:.3f}")
