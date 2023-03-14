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


print(todos_binarios)

with open('compactar.dv1', 'w') as arquivo:
    arquivo.write(str(ordenado))

with open('compactar.dv2', 'w') as arquivo:
    for elem in range(0, int(len(todos_binarios)/8)):
        aux = '0b' + todos_binarios[8 * elem: 8 * (elem + 1)]
        arquivo.write(chr(int(aux, 2)))
