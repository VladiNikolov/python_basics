number_one = int(input())
number_two = int(input())
operator = input()
even_or_odd = ""
result = 0

if operator == "+" :
    result = number_one + number_two
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
elif operator == "-":
    result = number_one - number_two
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
elif operator == "*":
    result = number_one * number_two
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"

if operator == "+" or operator == "-" or operator == "*":
    print(f"{number_one} {operator} {number_two} = {result} - {even_or_odd}")
elif operator == "/":
    if number_one == 0 or number_two == 0:
        print(f"Cannot divide {number_one} by zero")
    else:
        result = number_one / number_two
        print(f"{number_one} / {number_two} = {result:.2f}" )
elif operator == "%":
    if number_one == 0 or number_two == 0:
        print(f"Cannot divide {number_one} by zero")
    else:
        result = number_one % number_two
        print(f"{number_one} % {number_two} = {result}")

