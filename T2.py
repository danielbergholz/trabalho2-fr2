# DANIEL GOBBI BERGHOLZ 16/0004551
# LUKAS NUNES DE SOUZA 17/0150381
# JOAO VITOR FONSECA DE LIMA 17/0014118
# TRABALHO 2 FUNDAMENTOS DE REDES 2

# o codigo a seguir foi feito sob o efeito de muita pressao e cafeina
# nao recomendo mexer em nada, so deus sabe como isso tudo aqui funciona

# bibliotecas usadas no codigo
from PIL import Image, ImageFilter
import numpy

#variaveis globais ******************************************
texto = open('texto.txt', 'r') # sample de texto do star wars
texto = texto.read()

ascii_code_alfabeto = []
for i in range(65, 123, 1):
    if i < 91 or i > 96:
        ascii_code_alfabeto.append(chr(i))

dict_alfabeto = {}
for i in range(len(ascii_code_alfabeto)):
    dict_alfabeto[ascii_code_alfabeto[i]] = ord(ascii_code_alfabeto[i])

#*************************************************************

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

def cesarimg():

	im = Image.open("im.jpg",'r')

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


def cesarTexto():

    # loop para usuario digitar numero de deslocamento de cesar
    while True:
        try:
            n = input('Qual sera o valor do deslocamento?\n')
            break
        except NameError:
            print 'Por favor, digite um numero\n'
    print 'A seguir o texto original:\n'
    print texto

    # algoritmo de cesar
    cifrado = []
    for i in range(len(texto)-1):
        if ((ord(texto[i]) < 65) or (ord(texto[i]) > 90 and ord(texto[i]) < 97) or (ord(texto[i]) > 122)):
            cifrado.append(texto[i])
        else:
            for j in range(len(ascii_code_alfabeto)):
                if ascii_code_alfabeto[j] == texto[i]:
                    cifrado.append(ascii_code_alfabeto[(j-n)%len(ascii_code_alfabeto)])
    print 'A seguir o texto cifrado:\n'
    print ''.join(cifrado)
    try:
       n = input('\nPressione ENTER para voltar ao menu\n')
    except SyntaxError:
        pass

def menu():
    while True:
        print '***************************************************************'
        print '\nSeja bem vindo ao programa de criptografia de texto e imagens'
        print '\nA SEGUIR OS ALGORITMOS DISPONIVEIS PARA IMAGEM:\n'
        print '1) Cesar\n2) DES\n3) AES\n'
        print 'A SEGUIR OS ALGORITMOS DISPONIVEIS PARA TEXTO:\n'
        print '4) Cesar\n5) Vigenere\n6) RSA\n7) DAS\n8) SHA-2\n9) Twofish\n10) Serpent\n11) DES\n12) AES\n13) 3DES\n14) Diffie-Helman'
        try:
            n = input('\nPor favor, selecione um algoritmo que voce gostaria de executar: (ENTER para sair)\n')
        except SyntaxError:
            print 'Saindo do programa...'
            break
        if n == 1:
        	cesarimg()
        elif n == 4:
            cesarTexto()

if __name__ == "__main__":
    menu()
