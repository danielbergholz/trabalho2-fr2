# DANIEL GOBBI BERGHOLZ 16/0004551
# LUKAS NUNES DE SOUZA 17/0150381
# JOAO VITOR FONSECA DE LIMA 17/0014118
# TRABALHO 2 FUNDAMENTOS DE REDES 2

# o codigo a seguir foi feito sob o efeito de muita pressao e cafeina
# nao recomendo mexer em nada, so deus sabe como isso tudo aqui funciona

# bibliotecas usadas no codigo
from PIL import Image, ImageFilter
from random import randint
import time
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


def trans(pc):
    b = list("abcdefghijklmnopqrstuvxwyz25197,.-")
    cont = 0
    i = 0

    while(i < 34):
        if(pc == b[i]):
            break
        else:
            cont+=1
        i+=1
    return cont

def trans2(n):
    l = list("abcdefghijklmnopqrstuvxwyz25197,.-")
    
    j = l[n]

    return j

def ven(olu, chave,tipo):
    olu = olu.lower()
    t = list(olu)
    r = list(chave)
    x = len(olu)
    y = len(chave)
    j = 0
    o = 0
    p = 0
    k = 0
    f = 0
    j2 = 0
    if(tipo == 1):
        print("CIFRAGEM")
        while(j < x):
            if(t[j] == ' '):
                c = 0
            else:
                p = trans(t[j])
                k = trans(r[o])
                o+=1
                f = ((p+k)%34)
                t[j] = trans2(f)
                if(o == y):
                    o = 0
            j+=1
    elif(tipo == 2):
        print("DECIFRAGEM")
        while(j2 < x):
            if(t[j2] == ' '):
                c = 0
            else:
                p = trans(t[j2])
                k = trans(r[o])
                o+=1
                f = ((p-k+34)%34)
                t[j2] = trans2(f)
                if(o == y):
                    o = 0
            j2+=1
    t = ''.join(t)
    return t 

def RSA(olu,tipo):
    p = 3
    q = 11
    n = p*q
    z = (p-1)*(q-1)
    e = 7
    d = 3
    olu = olu.lower()
    t = list(olu)
    x = len(olu)
    j = 0
    r = 0
    i = 0
    if(tipo == 1):
        while(j < x):
            if(t[j] == ' '):
                c = 0
            else:
                m = trans(t[j])
                r = (m**e)%n
                t[j] = trans2(r)
            j+=1
    else:
        while(i < x):
            if(t[i] == ' '):
                c = 0
            else:
                m = trans(t[i])
                r =((m**d)%n)
                t[i] = trans2(r)
            i+=1 
    t = ''.join(t)
    return t
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

    x = int(input("Digite o valor desejado: "))

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
    im.close()

def DESimg():
    im = Image.open('im.jpg','r')

    arq = open('IV.txt', 'w')

    c1, c2 = im.size

    p1 = []
    p2 = []

    pix = im.load()

    # Aqui geramos os numeros aleatorios e colocamos no arquivo, sao as primeiras 6400 chaves
    # A imagem tem 640² pixels e dividos em 64 partes resultando 64 blocos de 6400 pixels cada

    for c in range (6400):
        x =  randint(0,255)
        p1.insert(c,x)
        arq.write(str(x))
        arq.write(" / ")

    arq.close()
    o = 0
    for i in range(c1):
        for j in range(c2):
            a, b, c = pix[i,j]
            ms = (a+b+c)/3
            zeta = int(ms)^p1[o]
            e = a^p1[o] 
            f = b^p1[o]
            g = c^p1[o]
            pix[i,j] = e,f,g
            p1[o] = zeta
            o+=1
            if(o == 6400):
                o = 0

    im.show()
    im.save("DES.jpg")
    im.close()

    
def AESimg(im):
    i = 2

def cesarTexto():

    # loop para usuario digitar numero de deslocamento de cesar
    while True:
        try:
            n = int(input('Qual sera o valor do deslocamento?\n'))
            break
        except NameError:
            print('Por favor, digite um numero\n')
    print('A seguir o texto original:\n')
    print(texto)

    # algoritmo de cesar
    cifrado = []
    for i in range(len(texto)-1):
        if ((ord(texto[i]) < 65) or (ord(texto[i]) > 90 and ord(texto[i]) < 97) or (ord(texto[i]) > 122)):
            cifrado.append(texto[i])
        else:
            for j in range(len(ascii_code_alfabeto)):
                if ascii_code_alfabeto[j] == texto[i]:
                    cifrado.append(ascii_code_alfabeto[(j+n)%len(ascii_code_alfabeto)])
    print('A seguir o texto cifrado:\n')
    print(''.join(cifrado))

# ALGORITMO DE DES PRA TEXTO

PI = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

CP_1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]

CP_2 = [14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32]

E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

S_BOX = [
         
[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
 [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
 [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
 [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
],

[[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
 [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
 [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
 [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
],

[[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
 [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
 [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
 [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
],

[[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
 [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
 [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
 [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
],  

[[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
 [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
 [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
 [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
], 

[[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
 [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
 [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
 [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
], 

[[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
 [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
 [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
 [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
],
   
[[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
 [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
 [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
 [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
]
]

P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]

PI_1 = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]

SHIFT = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

def string_to_bit_array(text):
    array = list()
    for char in text:
        binval = binvalue(char, 8)
        array.extend([int(x) for x in list(binval)])
    return array

def bit_array_to_string(array): 
    res = ''.join([chr(int(y,2)) for y in [''.join([str(x) for x in _bytes]) for _bytes in  nsplit(array,8)]])   
    return res

def binvalue(val, bitsize): 
    binval = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]
    if len(binval) > bitsize:
        raise "binary value larger than the expected size"
    while len(binval) < bitsize:
        binval = "0"+binval 
    return binval

def nsplit(s, n):
    return [s[k:k+n] for k in range(0, len(s), n)]

ENCRYPT=1
DECRYPT=0

class des():
    def __init__(self):
        self.password = None
        self.text = None
        self.keys = list()
        
    def run(self, key, text, action=ENCRYPT, padding=False):
        if len(key) < 8:
            raise "Key Should be 8 bytes long"
        elif len(key) > 8:
            key = key[:8] 
        
        self.password = key
        self.text = text
        
        if padding and action==ENCRYPT:
            self.addPadding()
        elif len(self.text) % 8 != 0:
            raise "Data size should be multiple of 8"
        
        self.generatekeys() 
        text_blocks = nsplit(self.text, 8)
        result = list()
        for block in text_blocks:
            block = string_to_bit_array(block)
            block = self.permut(block,PI)
            g, d = nsplit(block, 32) 
            tmp = None
            for i in range(16): 
                d_e = self.expand(d, E) 
                if action == ENCRYPT:
                    tmp = self.xor(self.keys[i], d_e)
                else:
                    tmp = self.xor(self.keys[15-i], d_e)
                tmp = self.substitute(tmp) 
                tmp = self.permut(tmp, P)
                tmp = self.xor(g, tmp)
                g = d
                d = tmp
            result += self.permut(d+g, PI_1) 
        final_res = bit_array_to_string(result)
        if padding and action==DECRYPT:
            return self.removePadding(final_res) 
        else:
            return final_res 
    
    def substitute(self, d_e):
        subblocks = nsplit(d_e, 6)
        result = list()
        for i in range(len(subblocks)): 
            block = subblocks[i]
            row = int(str(block[0])+str(block[5]),2)
            column = int(''.join([str(x) for x in block[1:][:-1]]),2) 
            val = S_BOX[i][row][column] 
            bin = binvalue(val, 4)
            result += [int(x) for x in bin]
        return result
        
    def permut(self, block, table):
        return [block[x-1] for x in table]
    
    def expand(self, block, table):
        return [block[x-1] for x in table]
    
    def xor(self, t1, t2):
        return [x^y for x,y in zip(t1,t2)]
    
    def generatekeys(self):
        self.keys = []
        key = string_to_bit_array(self.password)
        key = self.permut(key, CP_1) 
        g, d = nsplit(key, 28) 
        for i in range(16):
            g, d = self.shift(g, d, SHIFT[i]) 
            tmp = g + d 
            self.keys.append(self.permut(tmp, CP_2)) 

    def shift(self, g, d, n): 
        return g[n:] + g[:n], d[n:] + d[:n]
    
    def addPadding(self):
        pad_len = 8 - (len(self.text) % 8)
        self.text += pad_len * chr(pad_len)
    
    def removePadding(self, data):
        pad_len = ord(data[-1])
        return data[:-pad_len]
    
    def encrypt(self, key, text, padding=False):
        return self.run(key, text, ENCRYPT, padding)
    
    def decrypt(self, key, text, padding=False):
        return self.run(key, text, DECRYPT, padding)

def DEStexto():
    key = "secret_k"
    text= "Star Wars e uma franquia do tipo space opera criada pelo cineasta George Lucas que conta com uma serie de oito filmes de fantasia cientifica. O primeiro filme foi lancado apenas com o titulo Star Wars em 25 de maio de 1977, e tornou-se um fenomeno mundial."
    d = des()
    r = d.encrypt(key,text)
    r2 = d.decrypt(key,r)

    print("Texto original: ", r2)
    print("Texto cifrado: %r" % r)

def voltar_menu():
    try:
        n = int(input('\nPressione ENTER para voltar ao menu\n'))
    except (ValueError, SyntaxError) as e:
        pass

def menu():
    while True:
        print('***************************************************************')
        print('\nSeja bem vindo ao programa de criptografia de texto e imagens')
        print('\nA SEGUIR OS ALGORITMOS DISPONIVEIS PARA IMAGEM:\n')
        print('1) Cesar\n2) DES\n3) AES\n')
        print('A SEGUIR OS ALGORITMOS DISPONIVEIS PARA TEXTO:\n')
        print('4) Cesar\n5) Vigenere\n6) RSA\n7) DAS\n8) SHA-2\n9) Twofish\n10) Serpent\n11) DES\n12) AES\n13) 3DES\n14) Diffie-Helman')
        try:
            n = int(input('\nPor favor, selecione um algoritmo que voce gostaria de executar: (ENTER para sair)\n'))
        except (ValueError, SyntaxError) as e:
            print('Saindo do programa...')
            break
        if n == 1:
            inicio = time.time()
            cesarimg()
            fim = time.time()
            print("\n\nTempo de execucação do algoritmo: ", fim-inicio)
            voltar_menu()
        elif n == 2:
            inicio = time.time()
            DESimg()
            fim = time.time()
            print("\n\nTempo de execucação do algoritmo: ", fim-inicio)
            voltar_menu()
        elif n == 4:
            inicio = time.time()
            cesarTexto()
            fim = time.time()
            print("\n\nTempo de execucação do algoritmo: ", fim-inicio)
            voltar_menu()
        elif n == 5:
            txt = "Star Wars e uma franquia do tipo space opera criada pelo cineasta George Lucas que conta com uma serie de oito filmes de fantasia cientifica. O primeiro filme foi lancado apenas com o titulo Star Wars em 25 de maio de 1977, e tornou-se um fenomeno mundial"
            chave = input("Digite a chave: ")
            inicio = time.time()
            b = ven(txt,chave,1)
            fim = time.time()
            c = ven(b,chave,2)
            print("CIFRADO: \n______________________________________________\n", b)
            print("DECIFRADO: \n_______________________________________________\n", c)
            print("\n\nTempo de execucação do algoritmo: ", fim-inicio)
            voltar_menu()
        elif n == 6:
            inicio = time.time()
            txt = "Star Wars e uma franquia do tipo space opera criada pelo cineasta George Lucas que conta com uma serie de oito filmes de fantasia cientifica. O primeiro filme foi lancado apenas com o titulo Star Wars em 25 de maio de 1977, e tornou-se um fenomeno mundial"
            ci = RSA(txt,1)
            fim = time.time()
            de = RSA(ci,2)

            print("CIFRADO: \n\n", ci)
            print("DECIFRADO: \n\n", de)
            print("\n\nTempo de execucação do algoritmo: ", fim-inicio)
        elif n == 11:
            inicio = time.time()
            DEStexto()
            fim = time.time()
            print("\n\nTempo de execucação do algoritmo: ", fim-inicio)
            voltar_menu()

if __name__ == "__main__":
    menu()

#algoritmo AES para texto
import pyaes
import time

chave = "a72 jds cnh asf r99 xx7 32s hfn!" # Uma chave aleatória de 256 bit (32 bytes)
textobase = "Star Wars é uma franquia do tipo space opera criada pelo cineasta George Lucas que conta com uma série de oito filmes de fantasia científica. O primeiro filme foi lançado apenas com o título Star Wars em 25 de maio de 1977, e tornou-se um fenômeno mundial."

t1 = time.time() #inicia a contagem do tempo para encriptar a mensagem 

chave = bytes(chave,'utf-8') # Convertendo a chave em Bytes

aes = pyaes.AESModeOfOperationCTR(chave) #operacao no modo CTR de criptografia
textocifrado = aes.encrypt(textobase) #processo de criptografia 

print (textocifrado) # Mostra o texto encriptado

print ("Tempo de execucao para encriptar:", time.time() - t1, "segundos") #mostra o tempo gasto para encriptar a mensagem

t2 = time.time() #inicia a contagem do tempo para decifrar a mensagem 

# DECODIFICACAO
aes = pyaes.AESModeOfOperationCTR(chave) #operacao no modo CTR de criptografia

decrypted = aes.decrypt(textocifrado)# O conteudo decodificado é binário, precisamos decodificar para texto

new = str(decrypted, 'ISO-8859-1') #Transforma de bytes para string

print (new == textobase) #Verifica se o texto decodificado é igual ao texto original e retorna True ou False
print (new) #mostra o texto decifrado
print ("Tempo de execucao para decodificar ", time.time() - t2) #mostra o tempo gasto para decifrar a mensagem
