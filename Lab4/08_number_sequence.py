# import sys
# count_of_number = int(input())
# min_sum = sys.maxsize
# max_sum = - sys.maxsize
# for number in range(count_of_number):
#     current_number = int(input())
#     if current_number > max_sum:
#         max_sum = current_number
#     if current_number < min_sum:
#         min_sum = current_number
# print(f"Max number: {max_sum}")
# print(f"Min number: {min_sum}")


count_of_number = int(input())
first_number = int(input())

min_sum = first_number
max_sum = first_number
for number in range(count_of_number - 1):
    current_number = int(input())
    if current_number > max_sum:
        max_sum = current_number
    if current_number < min_sum:
        min_sum = current_number
print(f"Max number: {max_sum}")
print(f"Min number: {min_sum}")


