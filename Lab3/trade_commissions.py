# town = input()   програмата работи
# sales = float(input())
#
# commission = 0.00
# if town == 'Sofia':
#     if 0 <= sales <= 500:
#         commission = 0.05
#         print(f'{commission * sales:.2f}')
#     elif 500 < sales <= 1000:
#         commission = 0.07
#         print(f'{commission * sales:.2f}')
#     elif 1000 < sales <= 10000:
#         commission = 0.08
#         print(f'{commission * sales:.2f}')
#     elif sales > 10000:
#         commission = 0.12
#         print(f'{commission * sales:.2f}')
#     else:
#         print('error')
# elif town == 'Varna':
#     if 0 <= sales <= 500:
#         commission = 0.045
#         print(f'{commission * sales:.2f}')
#     elif 500 < sales <= 1000:
#         commission = 0.075
#         print(f'{commission * sales:.2f}')
#     elif 1000 < sales <= 10000:
#         commission = 0.10
#         print(f'{commission * sales:.2f}')
#     elif sales > 10000:
#         commission = 0.13
#         print(f'{commission * sales:.2f}')
#     else:
#         print('error')
# elif town == 'Plovdiv':
#     if 0 <= sales <= 500:
#         commission = 0.055
#         print(f'{commission * sales:.2f}')
#     elif 500 < sales <= 1000:
#         commission = 0.08
#         print(f'{commission * sales:.2f}')
#     elif 1000 < sales <= 10000:
#         commission = 0.12
#         print(f'{commission * sales:.2f}')
#     elif sales > 10000:
#         commission = 0.145
#         print(f'{commission * sales:.2f}')
#     else:
#         print('error')
# else:
#     print('error')

town = input() # програмата работи: решение с булеви
sales = float(input())

commission = 0.00
is_valid = True
if town == 'Sofia':
    if sales < 0:
        is_valid = False
    elif sales >= 0 and sales <= 500:
        commission = sales * 0.05
    elif sales <= 1000:
        commission = sales * 0.07
    elif sales <= 10000:
        commission = sales * 0.08
    elif sales > 10000:
        commission = sales * 0.12
elif town == 'Varna':
    if sales < 0:
        is_valid = False
    elif sales >= 0 and sales <= 500:
        commission = sales * 0.045
    elif sales <= 1000:
        commission = sales * 0.075
    elif sales <= 10000:
        commission = sales *  0.10
    elif sales > 10000:
        commission = sales *  0.13
elif town == 'Plovdiv':
    if sales < 0:
        is_valid = False
    elif sales >= 0 and sales <= 500:
        commission = sales *  0.055
    elif sales <= 1000:
        commission = sales * 0.08
    elif sales <= 10000:
        commission = sales * 0.12
    elif sales > 10000:
        commission = sales * 0.145
else:
    is_valid = False

if is_valid:
    print(f'{commission:.2f}')
else:
    print('error')





