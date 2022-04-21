all_price_from_sale = int(input())
pay_cash = 0
pay_card = 0
count_cash = 0
count_card = 0
counter = 0

while True:
    collected_money = pay_card + pay_cash
    if collected_money >= all_price_from_sale:
        print(f"Average CS: {pay_cash / count_cash:.2f}")
        print(f"Average CC: {pay_card / count_card:.2f}")
        break

    command = input()

    if command == 'End':
        print('Failed to collect required money for charity.')
        break

    current_number = int(command)
    counter += 1
    is_cash_payment = counter % 2 == 1

    if current_number <= 100 and is_cash_payment:
        pay_cash = pay_cash + current_number
        count_cash += 1
    elif current_number >= 10 and not is_cash_payment:
        pay_card = pay_card + current_number
        count_card += 1
    else:
        print(f'Error in transaction!')
        continue

    print("Product sold!")




# expected_sum = int(input())
#
#
#
# sold_cash = 0
#
# sold_card = 0
#
# total_cash = 0
#
# total_card = 0
#
# product_count = 0
#
#
#
# while True:
#
#     if total_cash + total_card >= expected_sum:
#
#         print(f'Average CS: {total_cash / sold_cash:.2f}')
#
#         print(f'Average CC: {total_card / sold_card:.2f}')
#
#         break
#
#
#
#     command = input()
#
#     if command == 'End':
#
#         print('Failed to collect required money for charity.')
#
#         break
#
#
#
#     price = int(command)
#
#
#
#     product_count += 1
#
#     is_cash_payment = product_count % 2 == 1
#
#
#
#     if price <= 100 and is_cash_payment:
#
#         total_cash += price
#
#         sold_cash += 1
#
#     elif price >= 10 and not is_cash_payment:
#
#         total_card += price
#
#         sold_card += 1
#
#     else:
#
#         print('Error in transaction!')
#
#         continue
#
#
#
#     print('Product sold!')
