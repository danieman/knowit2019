from collections import defaultdict


def move(src, dst):
    global visited
    global minutes
    
    cur_x, cur_y = src
    new_x, new_y = dst
    
    x_step = 1 if cur_x < new_x else -1
    y_step = 1 if cur_y < new_y else -1
    
    while cur_x != new_x:
        cur_x += x_step
        visited[(cur_x, cur_y)] += 1
        minutes += visited[(cur_x, cur_y)]
    
    while cur_y != new_y:
        cur_y += y_step
        visited[(cur_x, cur_y)] += 1
        minutes += visited[(cur_x, cur_y)]


coords = [(int(a), int(b)) for a, b in 
    [line.strip().split(',') for line in open('coords.csv').readlines()][1:]]
visited = defaultdict(int)
minutes = 0
src = (0, 0)

while coords:
    dst = coords.pop(0)
    move(src, dst)
    # print(f'{minutes:6}\': Moved from {src} to {dst}')
    src = dst

print()
print(minutes)