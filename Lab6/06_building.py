number_flours = int(input())
number_flats = int(input())

for flours in range(number_flours, 0, - 1):
    for flats in range(0, number_flats):

        if flours == number_flours:
            print(f'L{flours}{flats}', end=' ')
        elif flours % 2 == 0:
            print(f'O{flours}{flats}', end=' ')
        elif flours % 2 != 0:
            print(f'A{flours}{flats}', end=' ')

    print()


