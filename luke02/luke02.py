water = 0
for line in open('world.txt').readlines():
    left = line.find('#')
    right = line.rfind('#')
    water += line[left:right].count(' ')

print(water)