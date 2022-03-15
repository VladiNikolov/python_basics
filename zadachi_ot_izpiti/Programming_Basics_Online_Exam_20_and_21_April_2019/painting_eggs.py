size_of_eggs = input()
colour_of_eggs = input()
number_of_partida = int(input())
price = 0
if size_of_eggs == 'Large':
    if colour_of_eggs == 'Red':
        price = number_of_partida * 16
    elif colour_of_eggs == 'Green':
        price = number_of_partida * 12
    elif colour_of_eggs == 'Yellow':
        price = number_of_partida * 9
elif size_of_eggs == 'Medium':
    if colour_of_eggs == 'Red':
        price = number_of_partida * 13
    elif colour_of_eggs == 'Green':
        price = number_of_partida * 9
    elif colour_of_eggs == 'Yellow':
        price = number_of_partida * 7
elif size_of_eggs == 'Small':
    if colour_of_eggs == 'Red':
        price = number_of_partida * 9
    elif colour_of_eggs == 'Green':
        price = number_of_partida * 8
    elif colour_of_eggs == 'Yellow':
        price = number_of_partida * 5
total_price = price * 0.65
print(f"{total_price:.2f} leva.")
