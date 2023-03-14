import arvore
from arvore import ArvoreNo


class Huffman:
    def __init__(self, vet):
        self._vet = vet

    @property
    def vet(self):
        return self._vet

    def isArovre(self, no):
        if type(no) is ArvoreNo:
            return True
        return False
    def retorna_valor(self, tup):
        if type(tup) is ArvoreNo:
            return int(tup.valor)
        return tup[1]

    def gera_arvore(self):
        zip1 = list(zip(self._vet.keys(), self._vet.values()))
        while len(zip1) != 1:
            if self.isArovre(zip1[0]):
                no1 = zip1[0]
            else:
                no1 = ArvoreNo(zip1[0][0], zip1[0][1])

            if self.isArovre(zip1[1]):
                no2 = zip1[1]
            else:
                no2 = ArvoreNo(zip1[1][0], zip1[1][1])

            stri = no1.chave + '+' + no2.chave
            cont = no1.valor + no2.valor
            no_raiz = ArvoreNo(stri, cont, esquerda=no1, direita=no2)

            zip1.pop(0)
            zip1.pop(0)

            aux = 0
            flag = 0
            if len(zip1) >= 1:
                while self.retorna_valor(zip1[aux]) < cont:
                    if aux >= len(zip1) - 1:
                        zip1.append(no_raiz)
                        flag = 1
                        break
                    aux += 1

            if flag == 0:
                zip1.insert(aux, no_raiz)

        return zip1[0]
