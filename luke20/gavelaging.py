def is_prime(n):
    if n == 2: return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True


alver = [1, 0, 0, 0, 0]
step = 1
direction = 1       # 1 for clockwise, -1 for counterclockwise
working_alv = 0

while step < 1_000_740:
    step += 1
    if is_prime(step):
        if sorted(alver)[0] != sorted(alver)[1]:
            working_alv = alver.index(min(alver))
            alver[working_alv] += 1
            continue
    
    if step % 28 == 0:
        direction *= -1
        working_alv = (working_alv + direction) % len(alver)
        alver[working_alv] += 1
        continue
    
    if step % 2 == 0:
        if sorted(alver)[-1] != sorted(alver)[-2]:
            if alver[(working_alv + direction) % 5] == max(alver):
                working_alv = (working_alv + 2*direction) % len(alver)
                alver[working_alv] += 1
                continue
    
    if step % 7 == 0:
        working_alv = 4
        alver[working_alv] += 1
        continue

    working_alv = (working_alv + direction) % len(alver)
    alver[working_alv] += 1

print(alver)
print(max(alver)-min(alver))