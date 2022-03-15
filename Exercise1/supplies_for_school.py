count_pen = int(input())
count_markers = int(input())
liters_detergent = int(input())
procent_discount = int(input())

pen = count_pen * 5.80
markers = count_markers * 7.20
detergent = liters_detergent * 1.20

all_materials = pen + markers + detergent
discount = (all_materials * procent_discount/100)
all_price = all_materials-discount
print(all_price)
