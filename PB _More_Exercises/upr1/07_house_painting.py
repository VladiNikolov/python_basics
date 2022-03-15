height_house_x = float(input())
length_house_y = float(input())
height_roof_house_h = float(input())

front_rear_walls = (height_house_x * height_house_x) * 2
front_rear_walls = front_rear_walls - (1.2 * 2)

left_right_walls = (height_house_x * length_house_y) * 2
left_right_walls = left_right_walls - ((1.5 * 1.5) * 2)

front_rear_roof = (height_house_x * height_roof_house_h) / 2
front_rear_roof = front_rear_roof * 2

left_right_roof = height_house_x * length_house_y * 2
area_walls = front_rear_walls + left_right_walls
area_roof = front_rear_roof + left_right_roof
total_wall_paint = area_walls / 3.4
total_roof_paint = area_roof / 4.3
print(f"{total_wall_paint:.2f}")
print(f"{total_roof_paint:.2f}")