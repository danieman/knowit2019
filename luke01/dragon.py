sheep = [int(n) for n in open("sau.txt").read().split(",")]

ds = 50 # Dragon size
s = 0   # Starved for s days
p = 0   # Sheep population from previous day

for i, n in enumerate(sheep):
    if (p + n) >= ds:
        p += (n - ds)
        ds += 1
        s = 0
    else:
        p = 0
        ds -= 1
        s += 1

    if s == 5:
        print(f'After {i} days, the dragon ate everybody!')
        break