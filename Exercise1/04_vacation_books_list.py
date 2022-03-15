all_pages = int(input())
pages_per_hour = int(input())
days = int(input())

total_pages = all_pages / pages_per_hour
all_hours = total_pages / days
print(round(all_hours))