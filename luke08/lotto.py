class Wheel:
    def __init__(self, wheel):
        self.wheel = wheel
        self.state = 0


def start_game():
    global coins
    while True:
        w = wheels[int(str(coins)[-1])]
        res = functions[w.wheel[w.state]]()
        w.state = (w.state + 1) % 4
        if res == 'STOP':
            break
        elif res is None:
            pass
        else:
            coins = res
    return coins


def pluss4():
    global coins
    return coins + 4


def pluss101():
    global coins
    return coins + 101


def minus9():
    global coins
    return coins - 9


def minus1():
    global coins
    return coins - 1


def reversersiffer():
    global coins
    return int(str(coins)[::-1]) if coins >= 0 else int(str(coins)[1:][::-1])*(-1)


def opp7():
    global coins
    while str(coins)[-1] != '7':
        coins += 1
    return coins


def gangemsd():
    global coins
    return coins * int(str(coins)[0]) if coins >= 0 else coins * int(str(coins)[1])


def delemsd():
    global coins
    return coins // int(str(coins)[0]) if coins >= 0 else coins // int(str(coins)[1])


def pluss1tilpar():
    global coins
    pos = True if coins >= 0 else False
    digits = [int(c) for c in str(coins)] if pos else [int(c) for c in str(coins)[1:]]
    for idx, digit in enumerate(digits):
        if digit % 2 == 0:
            digits[idx] += 1
    number = int(''.join([str(d) for d in digits]))
    return number if pos else number*(-1)


def trekk1fraodde():
    global coins
    pos = True if coins >= 0 else False
    digits = [int(c) for c in str(coins)] if pos else [int(c) for c in str(coins)[1:]]
    for idx, digit in enumerate(digits):
        if digit % 2:
            digits[idx] -= 1
    number = int(''.join([str(d) for d in digits]))
    return number if pos else number*(-1)


def roterpar():
    global wheels
    for i in range(0, 10, 2):
        wheels[i].state = (wheels[i].state + 1) % 4


def roterodde():
    global wheels
    for i in range(1, 10, 2):
        wheels[i].state = (wheels[i].state + 1) % 4


def roteralle():
    global wheels
    for w in wheels:
        w.state = (w.state + 1) % 4


def stopp():
    return 'STOP'


def main():
    global payouts
    global wheels
    global coins

    with open('wheels.txt') as f:
        for line in f.readlines():
            w = [s.lower() for s in line.strip().split(': ')[1].split(', ')]
            wheels.append(Wheel(w))

    for i in range(1, 11):
        coins = i
        payouts.append(start_game())
        for w in wheels:
            w.state = 0
        print(payouts)

    print(max(payouts))


payouts = [0]
wheels = []
coins = 0
functions = {
    'pluss4': pluss4,
    'pluss101': pluss101,
    'minus9': minus9,
    'minus1': minus1,
    'reversersiffer': reversersiffer,
    'opp7': opp7,
    'gangemsd': gangemsd,
    'delemsd': delemsd,
    'pluss1tilpar': pluss1tilpar,
    'trekk1fraodde': trekk1fraodde,
    'roterpar': roterpar,
    'roterodde': roterodde,
    'roteralle': roteralle,
    'stopp': stopp
}


if __name__ == '__main__':
    main()