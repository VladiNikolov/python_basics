length_w = float(input())
width_l = float(input())


length_w_santimeters = length_w * 100
width_l_santimeters = (width_l - 1) * 100

count_desk_length = length_w_santimeters // 120
count_desk_width = width_l_santimeters // 70
all_desk = count_desk_length * count_desk_width - 3
print(all_desk)
#print(int(all_desk))