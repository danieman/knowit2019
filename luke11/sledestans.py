def length(stripe, speed):
    kilometres = 0
    ice_in_row = 0
    onmountain = False
    
    for terrain in stripe:
        kilometres += 1

        if terrain != 'I':
            ice_in_row = 0

        if terrain == 'G':
            speed -= 27
        elif terrain == 'I':
            ice_in_row += 1
            speed += (12 * ice_in_row)
        elif terrain == 'A':
            speed -= 59
        elif terrain == 'S':
            speed -= 212
        elif terrain == 'F':
            if onmountain:
                speed += 35
                onmountain = False
            else:
                speed -= 70
                onmountain = True

        if speed <= 0:
            return kilometres


print(length(open('terreng.txt').read(), 10703437))