length = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume_aquarium = length * width * height
volume_liters = volume_aquarium * 0.001 # volume_liters = volume_aquarium / 1000
percent = percent / 100
needed_liters = volume_liters * (1 - percent)
print(needed_liters)