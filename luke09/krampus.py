def iskrampus(n):
    """Checks for krampusness by string conversion"""
    s = str(n ** 2)
    for i in range(1, len(s)):
        a, b = int(s[:i]), int(s[i:])
        if a + b == n and b: return True
    return False


def mat(n):
    """Checks for krampusness without string conversion"""
    i = 10
    while n ** 2 // i != 0:
        a, b = n ** 2 // i, n ** 2 % i
        if a + b == n and b: return True
        i *= 10
    return False


print(sum([n for n in [int(l) for l in open('krampus.txt').readlines()] if mat(n)]))