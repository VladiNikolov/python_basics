number_eggs_first_player = int(input())
number_eggs_second_player = int(input())
command = input()

eggs_first = number_eggs_first_player
eggs_second = number_eggs_second_player

while command != 'End of battle':
    if command == "one":
        eggs_second = eggs_second - 1
    elif command == "two":
        eggs_first = eggs_first - 1

    if eggs_first == 0 or eggs_second == 0:
        break
    command = input()

if eggs_first == 0:
    print(f'Player one is out of eggs. Player two has {eggs_second} eggs left.')
elif eggs_second == 0:
    print(f'Player two is out of eggs. Player one has {eggs_first} eggs left.')
else:
    print(f"Player one has {eggs_first} eggs left.")
    print(f"Player two has {eggs_second} eggs left.")
