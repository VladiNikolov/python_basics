number_eggs_first_player = int(input())
number_eggs_second_player = int(input())


eggs_first = number_eggs_first_player
eggs_second = number_eggs_second_player
while command != 'End of battle':
    command = input()
    if command == 'End of battle':
        print(f"Player one has {eggs_first} eggs left.")
        print(f"Player two has {eggs_second} eggs left.")
        break
    elif eggs_second > 0 and command == 'one':
        eggs_second -= 1
    elif eggs_first > 0 and command == 'two':
        eggs_first -= 1
    if eggs_first == 0:
        print(f'Player one is out of eggs. Player two has {eggs_second} eggs left.')
    elif eggs_second == 0:
        print(f'Player two is out of eggs. Player one has {eggs_first} eggs left.')






