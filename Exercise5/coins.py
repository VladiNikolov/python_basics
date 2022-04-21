current_sum = float(input())
current_sum = int(current_sum * 100)
coins_counter = 0
coins_counter += current_sum // 200  # coins_counter = coins_counter + current_sum // 200
current_sum %= 200  #current_sum = current_sum % 200
coins_counter += current_sum // 100
current_sum %= 100
coins_counter += current_sum // 50  # coins_counter = coins_counter + current_sum // 200
current_sum %= 50
coins_counter += current_sum // 20  # coins_counter = coins_counter + current_sum // 200
current_sum %= 20
coins_counter += current_sum // 10  # coins_counter = coins_counter + current_sum // 200
current_sum %= 10
coins_counter += current_sum // 5  # coins_counter = coins_counter + current_sum // 200
current_sum %= 5
coins_counter += current_sum // 2  # coins_counter = coins_counter + current_sum // 200
current_sum %= 2
coins_counter += current_sum // 1  # coins_counter = coins_counter + current_sum // 200
current_sum %= 1
print(coins_counter)

# решение с if и while
# current_sum = float(input())
# current_sum = int(current_sum * 100) # превръща в цяло число
# coins_counter = 0
# while current_sum > 0:
#     if current_sum >= 200:
#         current_sum = current_sum - 200
#         coins_counter = coins_counter + 1
#     elif current_sum >= 100:
#         current_sum = current_sum - 100
#         coins_counter = coins_counter + 1
#     elif current_sum >= 50:
#         current_sum = current_sum - 50
#         coins_counter = coins_counter + 1
#     elif current_sum >= 20:
#         current_sum = current_sum - 20
#         coins_counter = coins_counter + 1
#     elif current_sum >= 10:
#         current_sum = current_sum - 10
#         coins_counter = coins_counter + 1
#     elif current_sum >= 5:
#         current_sum = current_sum - 5
#         coins_counter = coins_counter + 1
#     elif current_sum >= 2:
#         current_sum = current_sum - 2
#         coins_counter = coins_counter + 1
#     elif current_sum >= 1:
#         current_sum = current_sum - 1
#         coins_counter = coins_counter + 1
# print(coins_counter)




















