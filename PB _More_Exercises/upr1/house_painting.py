hight_x = float(input())
lendth_y = float(input())
roof_hight_h = float(input())

wall_left_right = (hight_x * lendth_y) * 2 #6*10*2=120
windows = (1.5 * 1.5) * 2  #1.5*1.5*2=4.5
area_wall_left_right = wall_left_right - windows #120-4.5=115.5

wall_front_rear = (hight_x * hight_x) * 2 #6*6*2=72
door = (2 * 1.2)   # 2*1.2=2.4
area_wall_front_rear = wall_front_rear - door  #72-2.4=69.6

roof_left_right = (hight_x * lendth_y) * 2 #6*10*2=120
roof_front_rear = (hight_x * roof_hight_h)  #формулата: страната по височината делено на 2

total_area_wall = area_wall_left_right + area_wall_front_rear
total_wall = total_area_wall / 3.4
total_area_roof = roof_left_right +roof_front_rear
total_roof = total_area_roof / 4.3

print(f'{total_wall:.2f}')
print(f'{total_roof:.2f}')
