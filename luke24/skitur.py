import subprocess
from PIL import Image


IMG_NO = 1


def create_image(coords, max_x, max_y):
    global IMG_NO
    im = Image.new('1', (max_x+1, max_y+1))
    for x, y in coords:
        im.putpixel((x, max_y-y), 1)
    im.save(f'{IMG_NO}.png')
    IMG_NO += 1


with open('turer.txt') as f:
    max_x = max_y = 0
    coords = []
    for line in f:
        try:
            x, y = [int(i) for i in line.split(',')]
            coords.append((int(x), int(y)))
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y
        except:
            create_image(coords, max_x, max_y)
            coords = []
            max_x = max_y = 0

subprocess.run(['convert', '+append', '1.png', '12.png', '18.png',
                '21.png', '32.png', '34.png', 'out.png'])
for i in range(1, 43):
    subprocess.run(['rm', f'{i}.png'])