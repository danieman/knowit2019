import sys
from collections import defaultdict

dict_container = [None]

with open('generations.txt') as f:
    lines = [line.strip().split(';') for line in f.readlines()]

antall_oddetallsalver = len(lines[0][1::2])
d = defaultdict(set)
for idx, parents in enumerate(lines[0]):
    parents = parents.split(',')
    if idx % 2:
        d[parents[0]].add(idx)
        d[parents[1]].add(idx)        
dict_container.append(d)

for i in range(1, 30):
    print(f'Generasjon {i}...')
    line = [alv.split(',') for alv in lines[i]]
    d = defaultdict(set)
    for idx, parents in enumerate(line):
        if str(idx) in dict_container[i].keys():
            d[parents[0]] = d[parents[0]].union(dict_container[i][str(idx)])
            d[parents[1]] = d[parents[1]].union(dict_container[i][str(idx)])

    alver = []
    for k, v in d.items():
        if len(v) == antall_oddetallsalver:
            alver.append(int(k))
    if alver:
        print(f'{i+1}:{min(alver)}')
        sys.exit(0)

    dict_container.append(d)
