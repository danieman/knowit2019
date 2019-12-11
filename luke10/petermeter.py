from collections import defaultdict
from datetime import datetime


months = {
    'Jan': 1,
    'Feb': 2,
    'Mar': 3,
    'Apr': 4,
    'May': 5,
    'Jun': 6,
    'Jul': 7,
    'Aug': 8,
    'Sep': 9,
    'Oct': 10,
    'Nov': 11,
    'Dec': 12
}

d = defaultdict(int)
sunday_shampoo = 0
wednesday_paper = 0

with open('logg.txt') as f:
    for line in f:
        if '*' not in line:
            dt = line.strip()[:-1].split()
            month, day = months[dt[0]], int(dt[1])
            date = datetime(2018, month, day)
        else:
            line = line.strip().split()
            amount, article = int(line[1]), line[-1]
            d[article] += amount
            if date.weekday() == 2 and article == 'toalettpapir':
                wednesday_paper += amount
            elif date.weekday() == 6 and article == 'sjampo':
                sunday_shampoo += amount

paste = d['tannkrem'] // 125
shamp = d['sjampo'] // 300
paper = d['toalettpapir'] // 25

print(paste, shamp, paper, sunday_shampoo, wednesday_paper)
print(paste * shamp * paper * sunday_shampoo * wednesday_paper)