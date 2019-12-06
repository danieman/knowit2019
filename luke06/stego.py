from PIL import Image

im = Image.open('mush.png')
mushed = list(reversed(im.getdata()))
orig = []

for i, (r, g, b) in enumerate(mushed[:-1]):
    px = (r ^ mushed[i+1][0],
          g ^ mushed[i+1][1],
          b ^ mushed[i+1][2])
    orig.append(px)

solution = Image.new('RGB', im.size)
solution.putdata(orig[::-1])
solution.save('original.png')