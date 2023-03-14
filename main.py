from arvore import ArvoreNo
from Huffman import Huffman

with open('teste.txt', 'r') as arquivo:
    texto = arquivo.read()

cont = {char: 0 for char in texto}
for char in texto:
    cont[char] = cont[char] + 1

ordenado = {char: valor for char, valor in sorted(cont.items(), key=lambda item: item[1])}
h1 = Huffman(ordenado)

aux = h1.gera_arvore()
aux.gera_binario(aux)

bi = {}
aux.retorna_bin(aux, bi)

todos_binarios = ""
for char in texto:
    todos_binarios = todos_binarios + bi[char]

#char = '0b' + todos_binarios[0:8]
#aux = chr(int(char, 2))
#print(bin(ord(aux)))

char = ""
for elem in range(8, len(todos_binarios), 8):
    aux = '0b' + todos_binarios[elem-8:elem]
    char = char + chr(int(aux,2))

with open('compactar.txt', 'w') as arquivo:
    arquivo.write(str(ordenado))
    arquivo.write(char)