from PIL import Image, ImageFilter
import numpy

def rot(v,x):
	i = 0
	if(x > 255):
		while(x > 255):
			v-=1
			x-=255
	elif(x < -255):
		while(x < -255):
			v+=1
			x+=255
	if(x == 0):
		return v
	else:
		if(x > 0):
			while(i < x):
				if((v+1) == 256):
					v = 0
				else:
					v+=1
				i+=1
		elif(x < 0):
			while(i > x):
				if((v-1) == -1):
					v = 255
				elif((v-1)!=-1):
					v-=1
				i-=1
	return v

def cesarimg(im):
	x = input("Digite o valor desejado: ")

	c1, c2 = im.size

	pix = im.load()

	q, w, r = pix[0,0]

	e = rot(q,x) 
	f = rot(w,x)
	g = rot(r,x)

	print(pix[0,0])

	for i in range(c1):
		for j in range(c2):
			a, b, c = pix[i,j]
			if((q == a) and (w==b) and (r==c)):
				pix[i,j] = e,f,g
			else:
				e = rot(a,x) 
				f = rot(b,x)
				g = rot(c,x)
				q,w,r = pix[i,j]
				pix[i,j] = e,f,g

	print(pix[0,0])
	im.show()
	im.save("cesar2.jpg")

def DESimg(im):
	i = 2

def AESimg(im):
	i = 2

imagem = Image.open("im.jpg",'r')

cesarimg(imagem)

DESimg(imagem)

AESimg(imagem)