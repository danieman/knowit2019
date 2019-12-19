import csv
from collections import Counter
from functools import reduce
from math import ceil, prod
from operator import mul
from string import ascii_lowercase


names = Counter()
d = {}
alph = ascii_lowercase

with open('names.txt') as f:
    d['male'], d['female'], d['p1'], d['p2'] = [l.strip().split('\n') for l in f.read().split('---')]

with open('employees.csv') as f:
    reader = csv.reader(f)
    next(reader)
    for line in reader:
        gender = 'male' if line[2] == 'M' else 'female'
        
        first_name = d[gender][sum([ord(c) for c in line[0]]) % len(d[gender])]
        
        last = ''.join(c for c in line[1] if c.isalpha())
        m = ceil(len(line[1]) / 2)
        last_1, last_2 = last[:m], last[m:]
        last_name = d['p1'][sum([alph.index(c.lower())+1 for c in last_1]) % len(d['p1'])]
        
        mult = prod([ord(c) for c in last_2])
        mult = mult * len(line[0]) if gender == 'male' else mult * len(line[0]+line[1])
        last_name += d['p2'][int(''.join(sorted(str(mult), reverse=True))) % len(d['p2'])]

        names[f'{first_name} {last_name}'] += 1

print(names.most_common(1)[0][0])