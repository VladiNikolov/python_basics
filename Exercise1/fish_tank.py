length = int(input())
width = int(input())
height = int(input())
procent = float(input())

volume = length * width * height
volume_liters = volume * 0.001
zaeto_prostranstvo = procent * 0.01
all_liters = volume_liters * ( 1 - zaeto_prostranstvo)
print(all_liters)


