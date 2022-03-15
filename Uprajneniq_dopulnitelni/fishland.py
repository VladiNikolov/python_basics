price_skumriq = float(input())
price_caca = float(input())
kg_palamud = float(input())
kg_safrid = float(input())
kg_midi = float(input())

palamud = price_skumriq * 1.6
price_palamud = kg_palamud * palamud

safrid = price_caca * 1.8
price_safrid = kg_safrid * safrid

price_midi = kg_midi * 7.50
all_price = price_palamud + price_safrid + price_midi
#print(round(all_price, 2))  #закръгляне до втория знак с функцията - round
print(f'{all_price:.2f}')  #форматиране до втория знак с print(f'{promenliva:.2f}')