from Crypto.Util.number import inverse


day = 7
code = inverse(day, 27644437) * 5897 % 27644437
print(code)