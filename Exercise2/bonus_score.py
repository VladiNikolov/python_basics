number = int(input())

bonus_point = 0 #нова променлива в която ще се изчислим натрупаните бонус точки
if number <= 100:
    bonus_point = 5
elif number > 1000:
    bonus_point = number * 0.1
else:
    bonus_point = number * 0.2
#изчисляване на допълнителните бонус точки
if number % 2 == 0:     #проверка за деление на четно число
    bonus_point +=1     #добави +1 към бонус точките
elif number % 10 == 5:  #проверка за деление и остотък 5
    bonus_point +=2     #добави +2 към бонус точките
print(bonus_point)
print(bonus_point + number)
