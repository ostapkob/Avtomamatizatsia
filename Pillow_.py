from PIL import ImageColor, Image, ImageDraw, ImageFont
import random
import subprocess
print(ImageColor.getcolor('red', 'RGBA'))
im = Image.open('Python.png')
change_size = im.resize((300,300))
# im.rotate(45).show()
change_size.save('resize_Python.png')

im3 = im.rotate(45, expand=True)
# im3.transpose((Image.FLIP_LEFT_RIGHT)).show()

rgb_im = im3.convert('RGB')
rgb_im.save('Python.jpg')

rgb_im = rgb_im.crop((800,700,900,800))  #CUT
im2 = Image.new('RGBA', (4000,2500), 'purple' )
im2.paste(rgb_im, (0,0))
im2.save('im2.png')

im2_w, im2_h = im2.size #b
im_h, im_w = rgb_im.size #s
# заполнить
for left in range(0, im2_w, im_w):
	for top in range(0, im2_h, im_h):
		im2.paste(rgb_im, (left,top))
im2.save('fill.png')	
#==========================================
# color pixels
print(im.getpixel((600,600))) # RGBA 
my_im = Image.new('RGBA', (255,255))
for x in range(100):
	r = random.randint(0,255)
	b = random.randint(0, 255)
	for y in range(255):
		g = random.randint(0, 255)
		my_im.putpixel((x,y), (r, x, b, y))
# my_im.show()
#==========================================
ss = 1.5
im_h,im_w = im.size
resiz =	im.resize((int(im_h/ss),int(im_w/ss)))
re_h, re_w = resiz.size
for n in range(0, 6):
	resiz = im.resize((int(im_h/ss),int(im_w/ss)))
	x = int(im_h/2-re_h/2)
	y = int(im_w/2-re_w/2)
	resiz = resiz.rotate(20)
	im.paste(resiz,(x,y),resiz )
im.save('test.png')
subprocess.Popen(['start', 'test.png'], shell=True) #  shell=True

#==========================================
dr_im = Image.new('RGBA', (200,200), 'grey')
draw = ImageDraw.Draw(dr_im)
draw.line([(0,0),(199,199)], fill='black')
draw.ellipse((120,30,160,60), fill='red')
for i in range(0,200,10):
	draw.line([(i,0), (200, i-10)], 'green')
my_font = ImageFont.truetype('MARSNEVENEKSK.otf', 32)
draw.text((10,160), 'Python', fill='black', font=my_font)
dr_im.show()

