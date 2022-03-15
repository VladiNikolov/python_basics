count_bottles = int(input())
detergent = count_bottles * 750
plates = 0
pots = 0
counter = 0

while detergent >= 0:
    command = input()

    if command == 'End':
        break
    dishes = int(command)
    counter += 1

    if counter % 3 == 0:
        pots = pots + dishes
        detergent = detergent - dishes * 15
    else:
        plates = plates + dishes
        detergent = detergent - dishes * 5
if detergent < 0:
    print(f'Not enough detergent, {abs(detergent)} ml. more necessary!')
else:
    print("Detergent was enough!")
    print(f"{plates} dishes and {pots} pots were washed.")
    print(f"Leftover detergent {detergent} ml.")