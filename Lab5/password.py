username = input()
reg_pass = input()

current_pass = input()
while current_pass != reg_pass:
    current_pass = input()

print('Welcome ' + username + '!')
