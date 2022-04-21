destination = input()

while destination != "End":
    budget = float(input())

    sum_current_destination = 0
    while sum_current_destination < budget:
        input_money = float(input())
        sum_current_destination += input_money

    print(f'Going to {destination}!')
    destination = input()


