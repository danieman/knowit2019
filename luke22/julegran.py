forest = open('forest.txt').readlines()

total_cashflow = 0
for y, line in enumerate(forest):
    for x, col in enumerate(line):
        try:
            if y == 0 and col == '#':
                total_cashflow += 40 * len(forest)
            elif col == '#':
                if forest[y][x-1] == ' ' and forest[y][x+1] == ' ' and forest[y-1][x] == ' ':
                    total_cashflow += 40 * (len(forest)-y)
        except:
            pass                    

print(total_cashflow)