class ArvoreNo:
    def __init__(self, chave, valor, esquerda=None, direita=None):
        self._chave = chave
        self._valor = valor
        self._esquerda = esquerda
        self._direita = direita

    @property
    def chave(self):
        return self._chave

    @property
    def valor(self):
        return self._valor

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

    """def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.chave,
                                   self.chave,
                                   self.direita and self.direita.chave)"""