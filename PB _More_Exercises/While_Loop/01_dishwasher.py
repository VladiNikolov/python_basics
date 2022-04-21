bottle_of_detergent = int(input())
all_detergent = bottle_of_detergent * 750
count_plates = 0
count_pots = 0
count_washing = 0
command = input()
while command != "End":
    current_input = int(command)
    count_washing += 1
    if command == "End":
        break
    if count_washing % 3 == 0:
        count_pots += current_input
        all_detergent = all_detergent - (current_input * 15)
    else:
        count_plates += current_input
        all_detergent = all_detergent - (current_input * 5)
    if all_detergent < 0:
        break
    command = input()
if all_detergent >= 0:
    print("Detergent was enough!")
    print(f"{count_plates} dishes and {count_pots} pots were washed.")
    print(f"Leftover detergent {all_detergent} ml.")
else:
    print(f"Not enough detergent, {abs(all_detergent)} ml. more necessary!")

