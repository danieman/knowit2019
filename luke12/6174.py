def count_iter(n):
    ctr = 0
    while int(n) != 6174:
        a = ''.join(sorted(str(n)))
        b = a[::-1]
        n = str(abs(int(a) - int(b))).zfill(4)
        ctr += 1
    return True if ctr == 7 else False

sevens = 0
for i in range(1000, 10000):
    if len(set(str(i))) == 1:
        continue
    sevens += count_iter(i)
print(sevens)