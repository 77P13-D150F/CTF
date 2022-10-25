#!/usr/bin/env python3

# Two images have to be combined to show the flag. https://en.wikipedia.org/wiki/Visual_cryptography

from PIL import Image

png1 = Image.open(r'C:\Users\RDOrsiEl\Downloads\scrambled1.png')
png2 = Image.open(r'C:\Users\RDOrsiEl\Downloads\scrambled2.png')
flag = Image.new(png1.mode, png1.size)

W, H = png1.size

for h in range(H):
    for w in range(W):
        r1, g1, b1 = png1.getpixel((w, h))
        r2, g2, b2 = png2.getpixel((w, h))
        r = (r1 + r2) % 256
        g = (g1 + g2) % 256
        b = (b1 + b2) % 256
        flag.putpixel((w, h), (r, g, b))

flag.show()
