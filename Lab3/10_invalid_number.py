# number = int(input())
#
# if 100 <= number <= 200 or number == 0:
#     print()
# else:
#     print("invalid")

num = int(input())

is_valid = (num >= 100 and num <= 200) or num == 0
if is_valid == True:
    print()
else:
    print("invalid")