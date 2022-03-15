degreece = float(input())

if 5 <= degreece <= 11.90:
    print("Cold")
elif 12.00 <= degreece <= 14.90:
    print("Cool")
elif 15.00 <= degreece <= 20.00:
    print("Mild")
elif 20.1 <= degreece <= 25.90:
    print("Warm")
elif 26.00 <= degreece <= 35.00:
    print("Hot")
else:
    print("unknown")