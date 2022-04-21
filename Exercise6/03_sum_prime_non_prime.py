command = input()
sum_prime_numbers = 0
sum_unequal_numbers = 0
is_positive_number = False
while command != "stop":
    current_number = int(command)
    if current_number < 0:
        print("Number is negative.")
    else:
        is_positive_number = True
        for number in range(2, current_number):
            if current_number % number == 0:
                is_positive_number = False
                break
        if is_positive_number:
            sum_prime_numbers += current_number
        else:
            sum_unequal_numbers += current_number
    command = input()

print(f"Sum of all prime numbers is: {sum_prime_numbers}")
print(f"Sum of all non prime numbers is: {sum_unequal_numbers}")