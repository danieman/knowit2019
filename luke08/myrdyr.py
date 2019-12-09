"""
This is the code of GitHub user @myrdyr (not mine!)
- Only saved it to keep it for reference (nice code - great learning!)
"""


PLUSS4         = lambda x: x+4
PLUSS101       = lambda x: x+101
MINUS9         = lambda x: x-9
MINUS1         = lambda x: x-1
REVERSERSIFFER = lambda x: int(str(abs(x))[::-1]) * (x/abs(x))
OPP7           = lambda x: [x+i for i in xrange(10) if str(x+i)[-1]=="7"][0]
GANGEMSD       = lambda x: x * int(str(abs(x))[0])
DELEMSD        = lambda x: x // int(str(abs(x))[0])
PLUSS1TILPAR   = lambda x: int(''.join(map(lambda y: str(int(y)+1) if y in "02468" else y, list(str(x)))))
TREKK1FRAODDE  = lambda x: int(''.join(map(lambda y: str(int(y)-1) if y in "13579" else y, list(str(x)))))
ROTERPAR       = lambda x: (x, map(lambda y: y.append(y.pop(0)) if wheels.index(y) % 2 == 0 else y, wheels))[0]
ROTERODDE      = lambda x: (x, map(lambda y: y.append(y.pop(0)) if wheels.index(y) % 2 == 1 else y, wheels))[0]
ROTERALLE      = lambda x: (x, map(lambda y: y.append(y.pop(0)), wheels))[0]
STOPP          = lambda x: stop

for init_coins in range(1, 11):
    coins = init_coins
    wheels = [eval("[" + line.rstrip().split(": ")[1] + "]") for line in open("wheels.txt").readlines()]
    wheel_ix = coins % 10
    while wheels[wheel_ix][0] != STOPP:
        coins = wheels[wheel_ix][0](coins)
        wheels[wheel_ix].append(wheels[wheel_ix].pop(0))
        wheel_ix = int(str(coins)[-1])
    print(init_coins, coins)