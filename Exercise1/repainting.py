nailon = int(input())
boq = int(input())
razreditel = int(input())
chasove = int(input())

price_nailon = (nailon + 2)  * 1.50
price_boq = (boq * 1.10) * 14.50
price_razreditel = razreditel * 5.00
torbichki = 0.40
all_meterials = price_nailon + price_boq + price_razreditel + torbichki
zaplata = all_meterials * 0.30 * chasove
total_razhodi = all_meterials + zaplata
print(total_razhodi)