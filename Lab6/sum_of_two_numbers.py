start = int(input())
end = int(input())
magic_num = int(input())

flag = False
count = 0
for i in range(start, end+1):
    for j in range(start, end+1):
        sum = i + j
        count += 1

        if sum == magic_num:
            print(f'Combination N:{count} ({i} + {j} = {sum})')
            flag = True
            break
    if flag:    #if flag == True:
        break
if not flag:
    print(f'{count} combinations - neither equals {magic_num}')