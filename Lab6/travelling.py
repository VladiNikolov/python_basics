destination = input()

while destination != 'End':
    price_trip = float(input())

    sum_current_destination = 0
    while sum_current_destination < price_trip:
        saved_money = float(input())
        sum_current_destination = sum_current_destination + saved_money

    print(f'Going to {destination}!')

    destination = input()