water = 0
for line in open('world.txt').readlines():
    water += line.strip().count(' ')
print(water)