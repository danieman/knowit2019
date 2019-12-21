def is_pal(n):
    return n == n[::-1]


def is_skjult(n):
    return is_pal(str(int(n) + int(n[::-1])))


count = 0
for i in range(123454322):
    n = str(i)
    if is_pal(n):
        continue
    elif is_skjult(n):
        count += i

print(count)