import PIL
from PIL import Image

img = Image.open("/Users/xiuli.j.shen/development/Erin+Zainab.jpg");
width, height = im.size

#img2 = img.crop((0, 0, 200, 200))
THUMBSIZE= 700, 700
img2 = img.thumbnail(THUMBSIZE, Image.ANTIALIAS) 

#half_the_width = img2.size[0] / 2
#half_the_height = img2.size[1] / 2
#img3 = img2.crop(
#    (
#        half_the_width - 50,
#        half_the_height - 75,
#        half_the_width + 50,
#        half_the_height + 75
#    )
#)

img.save("/Users/xiuli.j.shen/development/img2.jpg", quality=95)

