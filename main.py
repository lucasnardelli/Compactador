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

with open('compactar.dv1', 'w') as arquivo:
    for item in ordenado:
        arquivo.write(f"{item}:{ordenado[item]},")

with open('compactar.dv2', 'w') as arquivo:
    for elem in range(0, int(len(todos_binarios)/8)):
        aux = '0b' + todos_binarios[8 * elem: 8 * (elem + 1)]
        arquivo.write(chr(int(aux, 2)))

with open ('compactar.dv1', 'r') as arquivo:
    ler = arquivo.read()

ler = ler.split(",")
ler.pop()
dicio = {}
for item in ler:
    aux = item.split(':')
    dicio[aux[0]] = int(aux[1])

with open('compactar.dv2', 'r') as arquivo:
    descomp = arquivo.read()

bicompleta = ''
for item in descomp:
    aux = bin(ord(item))[2:]
    while len(aux) < 8:
        aux = '0' + aux
    bicompleta = bicompleta + aux

h2 = Huffman(dicio)

arv = h2.gera_arvore()
arv.gera_binario(arv)

bi2 = {}
arv.retorna_bin(arv, bi2)

char = ''
stringCompleta = ''

for elem in bicompleta:
    char += elem
    for chave, valor in bi2.items():
        if char == valor:
            stringCompleta += chave
            char = ''

with open('retorno.txt', 'w') as arquivo:
    arquivo.write(stringCompleta)