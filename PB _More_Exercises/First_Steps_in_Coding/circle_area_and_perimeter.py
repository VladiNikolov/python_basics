import math

radius = float(input())

area = math.pi * radius * radius #лице на окръжност формула: S=pi*r*r
perimetur = 2 * math.pi * radius #периметър на окръжност формула: P=2*pi*r

print(f'{area:.2f}')
print(f'{perimetur:.2f}')