from PIL import Image


with open('fjord.txt') as f:
    fjord = [line.strip() for line in f]

bits = [0 if sq == '#' else 1 for line in fjord for sq in line]

im = Image.new('1', (len(fjord[0]), len(fjord)))
im.putdata(bits)
im.save('fjord.png')