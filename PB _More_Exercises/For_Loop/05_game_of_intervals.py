moves = int(input())
result = 0
percent_1= 0
percent_2= 0
percent_3= 0
percent_4= 0
percent_5= 0
invalid = 0
for number in range(moves):
    current_move = int(input())
    if current_move < 0 or current_move > 50:
        result = result / 2
        invalid += 1
    elif current_move <= 9:
        result = result + (current_move * 0.20)
        percent_1 += 1
    elif current_move <= 19:
        result = result + (current_move * 0.30)
        percent_2 += 1
    elif current_move <= 29:
        result = result + (current_move * 0.40)
        percent_3 += 1
    elif current_move <= 39:
        result = result + 50
        percent_4 += 1
    elif 40 <= current_move <= 50:
        result = result + 100
        percent_5 += 1
print(f"{result:.2f}")
print(f"From 0 to 9: {percent_1 / moves * 100:.2f}%")
print(f"From 10 to 19: {percent_2 / moves * 100:.2f}%")
print(f"From 20 to 29: {percent_3 / moves * 100:.2f}%")
print(f"From 30 to 39: {percent_4 / moves * 100:.2f}%")
print(f"From 40 to 50: {percent_5 / moves * 100:.2f}%")
print(f"Invalid numbers: {invalid / moves * 100:.2f}%")




