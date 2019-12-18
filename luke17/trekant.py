t_ctr = t = inc = total = 0

while t_ctr <= 1_000_000:
    s = str(t)
    t += (inc+1)
    inc += 1
    t_ctr += 1
    for _ in range(len(s)):
        if int(s)**0.5 == int(int(s)**0.5):
            total += 1
            break
        s = s[1:]+s[0]

print(total)