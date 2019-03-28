import random
import wand
from flat import rgb, font, shape, strike, document, command

r=random
red = rgb(255, 0, 0)
#lato = font.open('Lato-Reg.otf')
figure = shape().stroke(red).width(0.5)
#headline = strike(lato).color(red).size(20, 24)

d = document(100, 100, 'mm')
p = d.addpage()
p.place(figure.circle(50, 50, 20))
p.place(figure.circle(50, 50, 20)).position(random.randint(50,50),random.randint(50,50))
d.pdf('hello.pdf')

from wand.image import Image as wi
pdf = wi(filename="hello.pdf", resolution=300)
pdfimage = pdf.convert("jpeg")
i=1
for img in pdfimage.sequence:
    page = wi(image=img)
    page.save(filename=str(i)+".jpg")
    i +=1