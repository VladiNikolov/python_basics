# number = int(input()) # с булева променлива
# counter = 1
# all_is_printed = False
#
# for row in range(1, number + 1):
#     for colums in range(1, row + 1):
#         print(counter, end=' ') # end = '\n'
#         counter += 1
#         if counter > number:
#             all_is_printed = True
#             break
#     if all_is_printed: #if all_is_printed = True:
#         break
#     print()

number = int(input())
counter = 1

for row in range(1, number + 1):
    for colums in range(1, row + 1):
        print(counter, end=' ')
        counter += 1
        if counter > number:
            break
    if counter > number:
        break
    print()
