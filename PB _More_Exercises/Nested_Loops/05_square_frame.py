number = int(input())
minus = "-"
num = number - 2

print(f"+" + " " + f"{minus} " * num + "+")
for i in range(num):
    print(f"|" + " " + f"{minus} " * num + "|")
print(f"+" + " " + f"{minus} " * num + "+")