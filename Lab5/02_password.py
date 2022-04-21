user_name = input()
password = input()

current_input = input()
while current_input != password:
    current_input = input()
print(f"Welcome {user_name}!")
