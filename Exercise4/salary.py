# open_tabs = int(input())
# salary = int(input())
#
# remaining_amount = 0
# for number in range(open_tabs):
#     sait_name = input()
#     if sait_name == 'Facebook':
#         remaining_amount = salary - 150
#     elif sait_name == 'Instagram':
#         remaining_amount = salary - 100
#     elif sait_name == 'Reddit':
#         remaining_amount = salary - 50
#     if salary <= 0:
#         break
# if salary <= 0:
#     print('You have lost your salary.')
# else:
#     difference = abs(salary-remaining_amount)
#     print(f'{difference}')

open_tabs = int(input())
salary = int(input())

remaining_amount = 0
for number in range(open_tabs):
    sait_name = input()
    if sait_name == 'Facebook':
        salary = salary - 150
    elif sait_name == 'Instagram':
        salary = salary - 100
    elif sait_name == 'Reddit':
        salary = salary - 50
    if salary <= 0:
        break
if salary <= 0:
    print('You have lost your salary.')
else:
    difference = abs(salary-remaining_amount)
    print(f'{difference}')

