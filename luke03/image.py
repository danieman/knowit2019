from PIL import Image

bits = [int(b) for b in open('input.txt').read()]
factors = [i for i in range(500, 1450) if 720720 % i == 0]
sizes = [(f, 720720//f) for f in factors]

ctr = 1
for size in sizes:
    img = Image.new('1', size)
    img.putdata(bits)
    img.save(f'ikea{ctr}.png')
    print(f'Created ikea{ctr}.png ({size[0]}x{size[1]})')
    ctr += 1