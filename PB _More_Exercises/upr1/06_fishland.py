# •	Първи ред – цена на скумрията на килограм. Реално число в интервала [0.00…40.00]
# •	Втори ред – цена на цацата на килограм. Реално число в интервала [0.00…30.00]
# •	Трети ред – килограма паламуд. Реално число в интервала [0.00…50.00]
# •	Четвърти ред – килограма сафрид. Реално число в интервала [0.00… 70.00]
# •	Пети ред – килограма миди. Цяло число в интервала [0 ... 100]

price_skumriq = float(input())
price_caca = float(input())
kilogram_palamud = float(input())
kilogram_safrid = float(input())
kilogram_midi = int(input())

price_palamud = price_skumriq * 1.6
price_safrid = price_caca * 1.8
price_midi = kilogram_midi * 7.50

total_price = price_midi + (price_palamud * kilogram_palamud) + (price_safrid * kilogram_safrid)
print(f"{total_price:.2f}")

