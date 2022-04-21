length_w = float(input())
width_h = float(input())

length_w_santimeters = length_w * 100
width_h_santimeters = (width_h - 1) * 100

count_desks_lenght = length_w_santimeters // 120
count_desks_width = width_h_santimeters // 70
all_desks = count_desks_lenght * count_desks_width - 3
print(all_desks)