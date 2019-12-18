with open('fjord.txt') as f:
    fjord = [line.strip('\n') for line in f]

for i, line in enumerate(fjord):
    if 'B' in line:
        b = (line.index('B'), i)
        fjord_length = len(line)

crosses = 1
direction = -1   # -1 for north, 1 for south

while b[0] < fjord_length-1:
    b = (b[0] + 1, b[1] + direction)
    if fjord[b[1]+3*direction][b[0]] == '#':
        b = (b[0]+1, b[1])
        direction *= -1
        crosses += 1

print(crosses)