tax = int(input())

basketball_sneakers = tax * 0.60
basketball_team = basketball_sneakers * 0.80
basketball_ball = basketball_team * 0.25
basketball_accessories = basketball_ball  * 0.20
all_price = basketball_accessories + basketball_ball + basketball_sneakers + basketball_team + tax
print(all_price)