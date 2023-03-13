from arvore import ArvoreNo
from Huffman import Huffman

with open('teste.txt', 'r') as arquivo:
    texto = arquivo.read()

cont = {char: 0 for char in texto}
for char in texto:
    cont[char] = cont[char] + 1

ordenado = {char: valor for char, valor in sorted(cont.items(), key=lambda item: item[1])}
print(ordenado)

h1 = Huffman(ordenado)
h1.gera_arvore()