sum = float(input())
mounth = int(input())
percent = float(input())

percent_per_mount = ((sum * percent) / 12) /100
total_sum = sum + (percent_per_mount * mounth)
print(total_sum)