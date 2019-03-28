import random
import wand
from fractions import Fraction 
from flat import rgb, font, shape, strike, document, command, image

import os, sys
from PIL import Image

from PIL import Image

basewidth = 20
img = Image.open('flower8.png')
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), Image.ANTIALIAS)
img.save('flower8.png')

f = Fraction(1, 2)

r=random
red = rgb(255, 0, 0)
#lato = font.open('Lato-Reg.otf')
figure = shape().stroke(red).width(0.5)
#headline = strike(lato).color(red).size(20, 24)
image = image.open('flower8.png')
pages = 5
elements = 12
d = document(190.5, 190.5, 'mm')
for page in range(pages):
  p = d.addpage()
  for element in range(elements):
   p.place(image).position(random.randint(1,100),random.randint(1,100))
  #p.place(figure.circle(50, 50, 20)).position(random.randint(1,100),random.randint(1,100))
  
d.pdf('hello.pdf')



from wand.image import Image as wi
pdf = wi(filename="hello.pdf", resolution=300)
pdfimage = pdf.convert("jpeg")
i=1
for img in pdfimage.sequence:
    page = wi(image=img)
    page.save(filename=str(i)+".jpg")
    i +=1
    
import imageio
images = []
filenames =['1.jpg',
'2.jpg',
'3.jpg',
'4.jpg',
'5.jpg']
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('movie.gif', images)