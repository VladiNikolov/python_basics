import sys

line = input()

max_num = -sys.maxsize
while line != 'Stop':
    current_num = int(line) # 99 100 80 70

    if current_num > max_num:
        max_num = current_num

    line = input() #ъпдейтване на променливата

print(max_num)