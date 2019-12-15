from itertools import cycle

alph = (2, 3, 5, 7, 11)
seq = []
sevens = 0

ctr = 0
for value in cycle(alph):
    if not seq:
        seq += [2]*2
    else:
        seq += [value]*seq[ctr]
        if value == 7:
            sevens += seq[ctr]
    ctr += 1
    if len(seq) == 217532235:
        break
print(7*sevens)