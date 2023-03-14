class ArvoreNo:
    def __init__(self, chave, valor, bi='', esquerda=None, direita=None):
        self._chave = chave
        self._valor = valor
        self._bi = bi
        self._esquerda = esquerda
        self._direita = direita

    @property
    def chave(self):
        return self._chave

    @property
    def valor(self):
        return self._valor

    @property
    def bi(self):
        return self._bi

    @bi.setter
    def bi(self, valor):
        self._bi = valor

    @property
    def esquerda(self):
        return self._esquerda

    @esquerda.setter
    def esquerda(self, valor):
        self._esquerda = valor

    @property
    def direita(self):
        return self._direita

    @direita.setter
    def direita(self, valor):
        self._direita = valor

    def obter_direita(self):
        return self._direita

    def obter_esquerda(self):
        return self._esquerda

    def gera_binario(self, no_atual):
        if no_atual is not None:
            if no_atual.obter_direita() is not None:
                no_atual.obter_direita().bi = no_atual.bi + '1'

            if no_atual.obter_esquerda() is not None:
                no_atual.obter_esquerda().bi = no_atual.bi + '0'

            self.gera_binario(no_atual.obter_esquerda())
            self.gera_binario(no_atual.obter_direita())

    def retorna_bin(self, no_atual, bi):
        if no_atual is not None:
            self.retorna_bin(no_atual.obter_esquerda(), bi)
            self.retorna_bin(no_atual.obter_direita(), bi)
            if len(no_atual.chave) == 1:
                bi[no_atual.chave] = no_atual.bi